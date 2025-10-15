"""
V4L2 Camera Controller
Handles camera detection, parameter management, and V4L2 communication
"""

import subprocess
import json
import logging
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
    
    def to_dict(self) -> Dict:
        """Convert parameter to dictionary for serialization"""
        return {
            'name': self.name,
            'value': self.value,
            'min_val': self.min_val,
            'max_val': self.max_val,
            'step': self.step,
            'param_type': self.param_type,
            'original_value': self.original_value
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
        return param

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
        self._detect_cameras()
    
    def _run_v4l2_command(self, command: List[str]) -> Tuple[bool, str]:
        """Run a v4l2 command and return success status and output"""
        try:
            result = subprocess.run(
                command, 
                capture_output=True, 
                text=True, 
                timeout=10
            )
            return result.returncode == 0, result.stdout
        except subprocess.TimeoutExpired:
            logger.error(f"Command timeout: {' '.join(command)}")
            return False, ""
        except Exception as e:
            logger.error(f"Command failed: {' '.join(command)}, Error: {e}")
            return False, ""
    
    def _detect_cameras(self):
        """Detect available V4L2 cameras"""
        logger.info("Detecting cameras...")
        
        if not IS_LINUX:
            logger.warning("Camera detection is only supported on Linux systems")
            # Create a dummy camera for Windows testing
            dummy_camera = CameraDevice("dummy0", "Dummy Camera (Windows Test)")
            dummy_camera.parameters = {
                "brightness": V4L2Parameter("brightness", 128, 0, 255, 1),
                "contrast": V4L2Parameter("contrast", 64, 0, 127, 1),
                "saturation": V4L2Parameter("saturation", 64, 0, 127, 1),
            }
            self.cameras["dummy0"] = dummy_camera
            return
        
        # Find video devices (Linux only)
        video_devices = []
        for i in range(10):  # Check /dev/video0 to /dev/video9
            device_path = f"/dev/video{i}"
            if Path(device_path).exists():
                video_devices.append(device_path)
        
        for device_path in video_devices:
            try:
                # Get device info
                success, output = self._run_v4l2_command([
                    "v4l2-ctl", "--device", device_path, "--info"
                ])
                
                if success and output:
                    # Extract device name from output
                    name_match = re.search(r"Card type\s*:\s*(.+)", output)
                    device_name = name_match.group(1).strip() if name_match else f"Camera {device_path}"
                    
                    camera = CameraDevice(device_path, device_name)
                    self.cameras[device_path] = camera
                    logger.info(f"Found camera: {camera}")
                    
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
        # Example: brightness 0x00980900 (int)    : min=0 max=255 step=1 default=128 value=128
        
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
        
        if not value_match:
            return None
        
        try:
            value = int(value_match.group(1))
            min_val = int(min_match.group(1)) if min_match else None
            max_val = int(max_match.group(1)) if max_match else None
            step = int(step_match.group(1)) if step_match else None
            
            return V4L2Parameter(
                name=param_name,
                value=value,
                min_val=min_val,
                max_val=max_val,
                step=step,
                param_type=param_type
            )
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