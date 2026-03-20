"""
V4L2 Camera Controller
Handles camera detection, parameter management, and V4L2 communication
"""

import subprocess
import shutil
import json
import logging
import os
import re
import platform
from typing import Dict, List, Optional, Tuple, Any
from pathlib import Path

logger = logging.getLogger(__name__)

# Platform detection
IS_LINUX = platform.system() == "Linux"
IS_WINDOWS = platform.system() == "Windows"

class V4L2Parameter:
    """Represents a V4L2 camera parameter"""
    
    def __init__(self, name: str, value: Any, min_val: Any = None, 
                 max_val: Any = None, step: Any = None, param_type: str = "int"):
        self.name = name
        self.value = value
        self.min_val = min_val
        self.max_val = max_val
        self.step = step
        self.param_type = param_type
        self.original_value = value  # For backup purposes
        self.is_readonly = False  # Whether parameter can be changed
        self.is_inactive = False  # Whether parameter is currently inactive
        self.flags = []  # V4L2 control flags
    
    def to_dict(self) -> Dict:
        """Convert parameter to dictionary for serialization"""
        return {
            'name': self.name,
            'value': self.value,
            'min_val': self.min_val,
            'max_val': self.max_val,
            'step': self.step,
            'param_type': self.param_type,
            'original_value': self.original_value,
            'is_readonly': self.is_readonly,
            'is_inactive': self.is_inactive,
            'flags': self.flags
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'V4L2Parameter':
        """Create parameter from dictionary"""
        param = cls(
            name=data['name'],
            value=data['value'],
            min_val=data.get('min_val'),
            max_val=data.get('max_val'),
            step=data.get('step'),
            param_type=data.get('param_type', 'int')
        )
        param.original_value = data.get('original_value', data['value'])
        param.is_readonly = data.get('is_readonly', False)
        param.is_inactive = data.get('is_inactive', False)
        param.flags = data.get('flags', [])
        return param
    
    @property
    def is_locked(self) -> bool:
        """Check if parameter is locked (readonly or inactive)"""
        return self.is_readonly or self.is_inactive

class CameraDevice:
    """Represents a V4L2 camera device"""
    
    def __init__(self, device_path: str, name: str):
        self.device_path = device_path
        self.name = name
        self.parameters: Dict[str, V4L2Parameter] = {}
        self.is_available = True
    
    def __str__(self):
        return f"{self.name} ({self.device_path})"

class CameraController:
    """Main controller for V4L2 camera operations"""
    
    def __init__(self):
        self.cameras: Dict[str, CameraDevice] = {}
        self._v4l2_ctl_path = self._find_v4l2_ctl()
        self._detect_cameras()
    
    def _find_v4l2_ctl(self) -> str:
        """Find the v4l2-ctl binary path"""
        # Try shutil.which first
        path = shutil.which("v4l2-ctl")
        if path:
            logger.debug(f"Found v4l2-ctl at: {path}")
            return path
        
        # Try common locations
        for candidate in ["/usr/bin/v4l2-ctl", "/usr/local/bin/v4l2-ctl", "/usr/sbin/v4l2-ctl"]:
            if Path(candidate).exists():
                logger.debug(f"Found v4l2-ctl at: {candidate}")
                return candidate
        
        logger.warning("v4l2-ctl not found in PATH or common locations")
        return "v4l2-ctl"  # Fall back to name, hope PATH works
    
    def _get_clean_env(self):
        """Get environment with LD_LIBRARY_PATH cleaned for external commands.
        
        PyInstaller sets LD_LIBRARY_PATH to its temp directory, which contains
        bundled libraries (e.g. libstdc++.so.6) that may be older than what
        system tools like v4l2-ctl require. We restore the original
        LD_LIBRARY_PATH so external commands use system libraries.
        """
        env = os.environ.copy()
        # PyInstaller saves the original value in *_ORIG
        orig = env.get('LD_LIBRARY_PATH_ORIG')
        if orig is not None:
            env['LD_LIBRARY_PATH'] = orig
        elif 'LD_LIBRARY_PATH' in env:
            del env['LD_LIBRARY_PATH']
        return env

    def _run_v4l2_command(self, command: List[str]) -> Tuple[bool, str]:
        """Run a v4l2 command and return success status and output"""
        # Replace 'v4l2-ctl' with full path if found
        if command and command[0] == "v4l2-ctl" and self._v4l2_ctl_path != "v4l2-ctl":
            command = [self._v4l2_ctl_path] + command[1:]
        
        try:
            result = subprocess.run(
                command, 
                capture_output=True, 
                text=True, 
                timeout=10,
                env=self._get_clean_env()
            )
            if result.returncode != 0 and result.stderr:
                logger.debug(f"Command stderr: {' '.join(command)}: {result.stderr.strip()}")
            return result.returncode == 0, result.stdout
        except subprocess.TimeoutExpired:
            logger.error(f"Command timeout: {' '.join(command)}")
            return False, ""
        except FileNotFoundError:
            logger.error(f"Command not found: {command[0]}")
            return False, ""
        except Exception as e:
            logger.error(f"Command failed: {' '.join(command)}, Error: {e}")
            return False, ""
    
    def _is_capture_device(self, device_path: str) -> bool:
        """Check if device is a video capture device"""
        try:
            # Method 1: Check device capabilities via --info (most reliable)
            success, output = self._run_v4l2_command([
                "v4l2-ctl", "--device", device_path, "--info"
            ])
            
            logger.debug(f"_is_capture_device({device_path}): --info success={success}, output_len={len(output) if output else 0}")
            if not success:
                logger.debug(f"_is_capture_device({device_path}): --info command failed")
            
            if success and output:
                # Log first few lines for debugging
                first_lines = output.strip().split('\n')[:5]
                logger.debug(f"_is_capture_device({device_path}): --info output: {first_lines}")
                
                output_lower = output.lower()
                # Check Device Caps or capabilities for video capture
                if "video capture" in output_lower:
                    logger.debug(f"_is_capture_device({device_path}): Found 'video capture' in --info output")
                    return True
            
            # Method 2: Check --list-formats output for capture type
            success, output = self._run_v4l2_command([
                "v4l2-ctl", "--device", device_path, "--list-formats"
            ])
            
            logger.debug(f"_is_capture_device({device_path}): --list-formats success={success}, output_len={len(output) if output else 0}")
            
            if success and output:
                logger.debug(f"_is_capture_device({device_path}): --list-formats output: {output.strip()[:200]}")
                output_lower = output.lower()
                if "video capture" in output_lower:
                    return True
                # Some devices list formats without explicit type header
                if re.search(r"\[\d+\]:", output):
                    return True
            
            # Method 3: Check if device has any controls (basic capture device check)
            success, output = self._run_v4l2_command([
                "v4l2-ctl", "--device", device_path, "--list-ctrls"
            ])
            
            logger.debug(f"_is_capture_device({device_path}): --list-ctrls success={success}, output_len={len(output) if output else 0}")
            
            if success and output and output.strip():
                logger.debug(f"_is_capture_device({device_path}): Device has controls, treating as capture device")
                return True
            
            logger.debug(f"_is_capture_device({device_path}): All methods failed, not a capture device")
            return False
        except Exception as e:
            logger.error(f"_is_capture_device({device_path}): Exception: {e}")
            return False
    
    def _check_preview_capability(self, device_path: str) -> bool:
        """Check if camera supports preview/streaming"""
        try:
            # Check supported formats
            success, output = self._run_v4l2_command([
                "v4l2-ctl", "--device", device_path, "--list-formats-ext"
            ])
            
            if not success:
                return False
            
            # Look for common video formats
            common_formats = ['YUYV', 'MJPG', 'RGB', 'YUV', 'H264', 'VP8', 'VP9']
            for fmt in common_formats:
                if fmt in output:
                    return True
            
            # Also check if device responds to capability query
            success, output = self._run_v4l2_command([
                "v4l2-ctl", "--device", device_path, "--all"
            ])
            
            return success and len(output.strip()) > 0
            
        except Exception:
            return False
    
    def _detect_cameras(self):
        """Detect available V4L2 cameras"""
        logger.info("Detecting cameras...")
        
        if not IS_LINUX:
            logger.warning("Camera detection is only supported on Linux systems")
            # Create a dummy camera for Windows testing
            dummy_camera = CameraDevice("dummy0", "Dummy Camera (Windows Test)")
            
            # Create some dummy parameters with different lock states
            brightness_param = V4L2Parameter("brightness", 128, 0, 255, 1)
            brightness_param.flags = ["slider"]
            
            exposure_auto_param = V4L2Parameter("exposure_auto", 1, 0, 3, 1)
            exposure_auto_param.flags = ["menu"]
            
            exposure_absolute_param = V4L2Parameter("exposure_absolute", 166, 1, 10000, 1)
            exposure_absolute_param.is_inactive = True
            exposure_absolute_param.flags = ["inactive"]
            
            focus_auto_param = V4L2Parameter("focus_auto", 1, 0, 1, 1)
            focus_auto_param.flags = ["button"]
            
            focus_absolute_param = V4L2Parameter("focus_absolute", 0, 0, 255, 5)
            focus_absolute_param.is_readonly = True
            focus_absolute_param.flags = ["read-only"]
            
            dummy_camera.parameters = {
                "brightness": brightness_param,
                "contrast": V4L2Parameter("contrast", 64, 0, 127, 1),
                "saturation": V4L2Parameter("saturation", 64, 0, 127, 1),
                "exposure_auto": exposure_auto_param,
                "exposure_absolute": exposure_absolute_param,
                "focus_auto": focus_auto_param,
                "focus_absolute": focus_absolute_param,
            }
            dummy_camera.is_available = True
            self.cameras["dummy0"] = dummy_camera
            return
        
        # Log v4l2-ctl location for debugging
        logger.debug(f"Using v4l2-ctl: {self._v4l2_ctl_path}")
        
        # Primary method: Use v4l2-ctl --list-devices to discover cameras
        cameras_found = self._detect_via_list_devices()
        
        if not cameras_found:
            logger.info("--list-devices found no cameras, trying /dev/video* scan...")
            self._detect_via_device_scan()
    
    def _detect_via_list_devices(self) -> bool:
        """Detect cameras using v4l2-ctl --list-devices"""
        success, output = self._run_v4l2_command([
            "v4l2-ctl", "--list-devices"
        ])
        
        logger.debug(f"--list-devices success={success}, output_len={len(output) if output else 0}")
        
        if not success or not output:
            logger.debug(f"--list-devices failed or empty output")
            return False
        
        logger.debug(f"--list-devices output:\n{output}")
        
        # Parse the output: camera name followed by indented device paths
        # Example:
        # USB Camera: USB Camera (usb-0000:00:12.0-1.1):
        #         /dev/video0
        #         /dev/video1
        #         /dev/media0
        current_group_key = None
        current_display_name = None
        device_groups = {}  # key -> (display_name, [device_paths])
        
        for line in output.split('\n'):
            line_stripped = line.strip()
            if not line_stripped:
                continue
            
            if not line.startswith('\t') and not line.startswith(' '):
                # This is a camera name line, e.g.:
                # USB Camera: USB Camera (usb-0000:00:12.0-1.1):
                # Use the full line (including USB path) as unique group key
                current_group_key = line_stripped.rstrip(':')
                # Extract clean display name (without USB path)
                name_match = re.match(r'^(.+?)\s*\(', current_group_key)
                current_display_name = name_match.group(1).strip() if name_match else current_group_key
            elif current_group_key and line_stripped.startswith('/dev/video'):
                # This is a device path
                if current_group_key not in device_groups:
                    device_groups[current_group_key] = (current_display_name, [])
                device_groups[current_group_key][1].append(line_stripped)
        
        logger.debug(f"Parsed device groups: {device_groups}")
        
        if not device_groups:
            return False
        
        # For each camera group, use the first /dev/video* device
        for group_key, (camera_name, device_paths) in device_groups.items():
            if not device_paths:
                continue
            
            # Use the first video device (typically the capture device)
            device_path = device_paths[0]
            logger.info(f"Probing camera: {camera_name} at {device_path}")
            
            # Verify it's accessible with --info
            success, info_output = self._run_v4l2_command([
                "v4l2-ctl", "--device", device_path, "--info"
            ])
            
            if not success:
                logger.warning(f"Cannot access {device_path}, trying next device in group")
                # Try other devices in the group
                for alt_path in device_paths[1:]:
                    if alt_path.startswith('/dev/video'):
                        success, info_output = self._run_v4l2_command([
                            "v4l2-ctl", "--device", alt_path, "--info"
                        ])
                        if success:
                            device_path = alt_path
                            break
            
            if not success:
                logger.warning(f"Cannot access any device for camera: {camera_name}")
                continue
            
            # Extract proper card name from --info output
            if info_output:
                name_match = re.search(r"Card type\s*:\s*(.+)", info_output)
                if name_match:
                    camera_name = name_match.group(1).strip()
            
            camera = CameraDevice(device_path, camera_name)
            camera.is_available = self._check_preview_capability(device_path)
            
            self.cameras[device_path] = camera
            logger.info(f"Found camera: {camera} (Preview: {'Yes' if camera.is_available else 'No'})")
            
            # Load initial parameters
            self._load_camera_parameters(camera)
        
        return len(self.cameras) > 0
    
    def _detect_via_device_scan(self):
        """Fallback: Detect cameras by scanning /dev/video* devices"""
        # Find video devices
        video_devices = []
        for i in range(20):
            device_path = f"/dev/video{i}"
            if Path(device_path).exists():
                video_devices.append(device_path)
        
        logger.debug(f"Found video devices: {video_devices}")
        
        for device_path in video_devices:
            try:
                if not self._is_capture_device(device_path):
                    logger.debug(f"Skipping {device_path} - not a capture device")
                    continue
                
                # Get device info
                success, output = self._run_v4l2_command([
                    "v4l2-ctl", "--device", device_path, "--info"
                ])
                
                if success and output:
                    name_match = re.search(r"Card type\s*:\s*(.+)", output)
                    device_name = name_match.group(1).strip() if name_match else f"Camera {device_path}"
                    
                    camera = CameraDevice(device_path, device_name)
                    camera.is_available = self._check_preview_capability(device_path)
                    
                    self.cameras[device_path] = camera
                    logger.info(f"Found camera: {camera} (Preview: {'Yes' if camera.is_available else 'No'})")
                    
                    # Load initial parameters
                    self._load_camera_parameters(camera)
                    
            except Exception as e:
                logger.warning(f"Failed to detect camera {device_path}: {e}")
    
    def _load_camera_parameters(self, camera: CameraDevice):
        """Load all available parameters for a camera"""
        logger.info(f"Loading parameters for {camera.name}")
        
        # Get list of controls
        success, output = self._run_v4l2_command([
            "v4l2-ctl", "--device", camera.device_path, "--list-ctrls"
        ])
        
        if not success:
            logger.warning(f"Failed to get controls for {camera.device_path}")
            return
        
        # Parse control output
        for line in output.split('\n'):
            if ':' in line and 'min=' in line:
                try:
                    param = self._parse_control_line(line)
                    if param:
                        camera.parameters[param.name] = param
                except Exception as e:
                    logger.warning(f"Failed to parse control line: {line}, Error: {e}")
    
    def _parse_control_line(self, line: str) -> Optional[V4L2Parameter]:
        """Parse a v4l2-ctl control line"""
        # Example: brightness 0x00980900 (int)    : min=0 max=255 step=1 default=128 value=128 flags=slider
        
        # Extract parameter name
        name_match = re.search(r"^\s*(\w+)", line)
        if not name_match:
            return None
        
        param_name = name_match.group(1)
        
        # Extract type
        type_match = re.search(r"\((\w+)\)", line)
        param_type = type_match.group(1) if type_match else "int"
        
        # Extract values
        value_match = re.search(r"value=([+-]?\d+)", line)
        min_match = re.search(r"min=([+-]?\d+)", line)
        max_match = re.search(r"max=([+-]?\d+)", line)
        step_match = re.search(r"step=([+-]?\d+)", line)
        flags_match = re.search(r"flags=([^\s]+)", line)
        
        if not value_match:
            return None
        
        try:
            value = int(value_match.group(1))
            min_val = int(min_match.group(1)) if min_match else None
            max_val = int(max_match.group(1)) if max_match else None
            step = int(step_match.group(1)) if step_match else None
            
            param = V4L2Parameter(
                name=param_name,
                value=value,
                min_val=min_val,
                max_val=max_val,
                step=step,
                param_type=param_type
            )
            
            # Parse flags
            if flags_match:
                flags_str = flags_match.group(1)
                param.flags = flags_str.split(',') if ',' in flags_str else [flags_str]
                
                # Check for readonly/inactive flags
                param.is_readonly = 'read-only' in param.flags or 'ro' in param.flags
                param.is_inactive = 'inactive' in param.flags or 'grabbed' in param.flags
            
            return param
            
        except ValueError as e:
            logger.warning(f"Failed to parse numeric values from line: {line}, Error: {e}")
            return None
    
    def get_cameras(self) -> List[CameraDevice]:
        """Get list of available cameras"""
        return list(self.cameras.values())
    
    def get_camera(self, device_path: str) -> Optional[CameraDevice]:
        """Get camera by device path"""
        return self.cameras.get(device_path)
    
    def set_parameter(self, device_path: str, param_name: str, value: Any) -> bool:
        """Set a camera parameter"""
        camera = self.cameras.get(device_path)
        if not camera:
            logger.error(f"Camera not found: {device_path}")
            return False
        
        if param_name not in camera.parameters:
            logger.error(f"Parameter not found: {param_name}")
            return False
        
        if not IS_LINUX:
            # Simulate parameter setting for Windows testing
            camera.parameters[param_name].value = value
            logger.info(f"[SIMULATED] Set {param_name}={value} for {camera.name}")
            return True
        
        # Set the parameter using v4l2-ctl (Linux only)
        success, output = self._run_v4l2_command([
            "v4l2-ctl", "--device", device_path, "--set-ctrl", f"{param_name}={value}"
        ])
        
        if success:
            camera.parameters[param_name].value = value
            logger.info(f"Set {param_name}={value} for {camera.name}")
            return True
        else:
            logger.error(f"Failed to set {param_name}={value} for {camera.name}")
            return False
    
    def get_parameter(self, device_path: str, param_name: str) -> Optional[Any]:
        """Get current value of a camera parameter"""
        camera = self.cameras.get(device_path)
        if not camera or param_name not in camera.parameters:
            return None
        
        # Get current value from camera
        success, output = self._run_v4l2_command([
            "v4l2-ctl", "--device", device_path, "--get-ctrl", param_name
        ])
        
        if success and output:
            # Parse output: "brightness: 128"
            value_match = re.search(rf"{param_name}:\s*([+-]?\d+)", output)
            if value_match:
                value = int(value_match.group(1))
                camera.parameters[param_name].value = value
                return value
        
        return camera.parameters[param_name].value
    
    def backup_parameters(self, device_path: str) -> bool:
        """Backup all current parameter values as original values"""
        camera = self.cameras.get(device_path)
        if not camera:
            return False
        
        for param in camera.parameters.values():
            current_value = self.get_parameter(device_path, param.name)
            if current_value is not None:
                param.original_value = current_value
        
        logger.info(f"Backed up parameters for {camera.name}")
        return True
    
    def restore_parameters(self, device_path: str) -> bool:
        """Restore all parameters to their original values"""
        camera = self.cameras.get(device_path)
        if not camera:
            return False
        
        success_count = 0
        for param in camera.parameters.values():
            if self.set_parameter(device_path, param.name, param.original_value):
                success_count += 1
        
        logger.info(f"Restored {success_count}/{len(camera.parameters)} parameters for {camera.name}")
        return success_count == len(camera.parameters)
    
    def refresh_camera(self, device_path: str):
        """Refresh camera parameters"""
        camera = self.cameras.get(device_path)
        if camera:
            self._load_camera_parameters(camera)
    
    def try_unlock_parameter(self, device_path: str, param_name: str) -> bool:
        """Try to unlock a parameter by disabling related auto modes"""
        camera = self.cameras.get(device_path)
        if not camera or param_name not in camera.parameters:
            return False
        
        param = camera.parameters[param_name]
        if not param.is_locked:
            return True  # Already unlocked
        
        # Define parameter unlock strategies
        unlock_strategies = {
            'exposure_absolute': ['exposure_auto'],
            'focus_absolute': ['focus_auto'],
            'white_balance_temperature': ['white_balance_temperature_auto'],
            'gain': ['gain_automatic'],
            'brightness': ['auto_exposure'],
            'contrast': ['auto_exposure'],
            'saturation': ['auto_exposure'],
        }
        
        # Try to disable auto modes that might lock this parameter
        auto_params = unlock_strategies.get(param_name, [])
        success = False
        
        for auto_param in auto_params:
            if auto_param in camera.parameters:
                # Try to set auto parameter to manual mode (usually 0)
                if self.set_parameter(device_path, auto_param, 0):
                    logger.info(f"Disabled {auto_param} to unlock {param_name}")
                    success = True
        
        # Also try some common auto parameters that might affect this one
        common_auto_params = ['exposure_auto', 'white_balance_temperature_auto', 'focus_auto', 'gain_automatic']
        for auto_param in common_auto_params:
            if auto_param in camera.parameters and auto_param not in auto_params:
                current_value = camera.parameters[auto_param].value
                if current_value != 0:  # If it's in auto mode
                    if self.set_parameter(device_path, auto_param, 0):
                        logger.info(f"Disabled {auto_param} (common auto) to unlock {param_name}")
                        success = True
        
        # Refresh parameters to check if unlock was successful
        if success:
            self._load_camera_parameters(camera)
            param = camera.parameters.get(param_name)
            return param and not param.is_locked
        
        return False
    
    def get_locking_parameters(self, device_path: str, param_name: str) -> List[str]:
        """Get list of parameters that might be locking the given parameter"""
        unlock_strategies = {
            'exposure_absolute': ['exposure_auto'],
            'focus_absolute': ['focus_auto'],
            'white_balance_temperature': ['white_balance_temperature_auto'],
            'gain': ['gain_automatic'],
            'brightness': ['auto_exposure'],
            'contrast': ['auto_exposure'],
            'saturation': ['auto_exposure'],
        }
        
        return unlock_strategies.get(param_name, [])