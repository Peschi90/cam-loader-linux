"""
Main GUI Window
Primary interface for the CamLoader application
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import logging
from typing import Optional

# Optional imports for different platforms
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False
    print("Warning: OpenCV (cv2) not available. Preview functionality will be limited.")

try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("Warning: PIL not available. Image processing will be limited.")

from camera.controller import CameraController, CameraDevice
from config.manager import ConfigManager
from gui.parameter_frame import ParameterFrame
from gui.preview_frame import PreviewFrame
from gui.startup_config import StartupConfigWindow

logger = logging.getLogger(__name__)

class CamLoaderMainWindow:
    """Main application window"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CamLoader - V4L2 Camera Controller")
        self.root.geometry("900x1000")  # Taller window for vertical layout
        
        # Controllers
        self.camera_controller = CameraController()
        self.config_manager = ConfigManager()
        
        # Current camera
        self.current_camera: Optional[CameraDevice] = None
        
        # GUI Components
        self.setup_ui()
        
        # Load saved configurations
        self.load_saved_configs()
        
        # Apply startup configurations
        self.apply_startup_configurations()
        
        # Setup window close handler
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_ui(self):
        """Setup the user interface"""
        # Create main menu
        self.create_menu()
        
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=2)  # Parameters get more space
        main_frame.rowconfigure(2, weight=1)  # Preview gets less space
        
        # Camera selection frame
        self.create_camera_selection_frame(main_frame)
        
        # Control panels
        self.create_control_panels(main_frame)
        
        # Give parameter frame access to camera controller for unlock functionality
        self.parameter_frame.set_camera_controller(self.camera_controller)
        
        # Status bar
        self.create_status_bar()
        
        # Load cameras
        self.refresh_cameras()
    
    def create_menu(self):
        """Create application menu"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save Configuration", command=self.save_config)
        file_menu.add_command(label="Load Configuration", command=self.load_config)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)
        
        # Camera menu
        camera_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Camera", menu=camera_menu)
        camera_menu.add_command(label="Refresh Cameras", command=self.refresh_cameras)
        camera_menu.add_command(label="Backup Parameters", command=self.backup_parameters)
        camera_menu.add_command(label="Restore Parameters", command=self.restore_parameters)
        camera_menu.add_separator()
        camera_menu.add_command(label="Startup Configuration...", command=self.show_startup_config)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
    
    def create_camera_selection_frame(self, parent):
        """Create camera selection frame"""
        selection_frame = ttk.LabelFrame(parent, text="Camera Selection", padding="5")
        selection_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Camera dropdown
        ttk.Label(selection_frame, text="Camera:").grid(row=0, column=0, padx=(0, 5))
        
        self.camera_var = tk.StringVar()
        self.camera_combo = ttk.Combobox(
            selection_frame, 
            textvariable=self.camera_var,
            state="readonly",
            width=50
        )
        self.camera_combo.grid(row=0, column=1, padx=(0, 10), sticky=(tk.W, tk.E))
        self.camera_combo.bind("<<ComboboxSelected>>", self.on_camera_selected)
        
        # Refresh button
        ttk.Button(
            selection_frame, 
            text="Refresh", 
            command=self.refresh_cameras
        ).grid(row=0, column=2, padx=(5, 0))
        
        selection_frame.columnconfigure(1, weight=1)
    
    def create_control_panels(self, parent):
        """Create main control panels"""
        # Parameters panel - now on top
        self.parameter_frame = ParameterFrame(parent, self.on_parameter_changed)
        self.parameter_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Preview panel - now below parameters
        self.preview_frame = PreviewFrame(parent)
        self.preview_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    def create_status_bar(self):
        """Create status bar"""
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(
            self.root, 
            textvariable=self.status_var, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        status_bar.grid(row=2, column=0, sticky=(tk.W, tk.E))
    
    def refresh_cameras(self):
        """Refresh available cameras"""
        self.status_var.set("Refreshing cameras...")
        
        try:
            # Reinitialize camera controller
            self.camera_controller = CameraController()
            cameras = self.camera_controller.get_cameras()
            
            # Update combo box
            camera_names = []
            for camera in cameras:
                name = str(camera)
                if not camera.is_available:
                    name += " [No Preview]"
                camera_names.append(name)
            
            self.camera_combo['values'] = camera_names
            
            if cameras:
                self.camera_combo.current(0)
                self.on_camera_selected()
                self.status_var.set(f"Found {len(cameras)} cameras")
            else:
                self.camera_combo.set("")
                self.current_camera = None
                self.parameter_frame.clear_parameters()
                self.preview_frame.stop_preview()
                self.status_var.set("No cameras found")
                
        except Exception as e:
            logger.error(f"Failed to refresh cameras: {e}")
            self.status_var.set("Error refreshing cameras")
            messagebox.showerror("Error", f"Failed to refresh cameras: {e}")
    
    def on_camera_selected(self, event=None):
        """Handle camera selection"""
        try:
            selection = self.camera_combo.get()
            if not selection:
                return
            
            # Convert to string to handle StringVar or string
            selection = str(selection)
            
            # Extract device path from selection
            if "(" not in selection or ")" not in selection:
                logger.warning(f"Invalid camera selection format: {selection}")
                return
            
            # Parse device path safely
            try:
                device_path = selection.split("(")[1].split(")")[0]
            except (IndexError, AttributeError) as parse_error:
                logger.error(f"Failed to parse device path from: {selection}, error: {parse_error}")
                return
                
            self.current_camera = self.camera_controller.get_camera(device_path)
            
            if self.current_camera:
                # Update parameter frame
                self.parameter_frame.set_camera(self.current_camera)
                
                # Update preview frame
                self.preview_frame.set_camera(device_path)
                
                # Load saved configuration if available
                self.load_camera_config()
                
                self.status_var.set(f"Selected: {self.current_camera.name}")
                logger.info(f"Selected camera: {self.current_camera}")
            
        except Exception as e:
            import traceback
            logger.error(f"Failed to select camera: {e}\n{traceback.format_exc()}")
            self.status_var.set("Error selecting camera")
            messagebox.showerror("Error", f"Failed to select camera: {e}")
    
    def on_parameter_changed(self, param_name: str, value):
        """Handle parameter value change"""
        if not self.current_camera:
            return
        
        try:
            success = self.camera_controller.set_parameter(
                self.current_camera.device_path, 
                param_name, 
                value
            )
            
            if success:
                self.status_var.set(f"Set {param_name} = {value}")
            else:
                self.status_var.set(f"Failed to set {param_name}")
                
        except Exception as e:
            logger.error(f"Failed to set parameter {param_name}: {e}")
            self.status_var.set("Error setting parameter")
    
    def backup_parameters(self):
        """Backup current camera parameters"""
        if not self.current_camera:
            messagebox.showwarning("Warning", "No camera selected")
            return
        
        try:
            success = self.camera_controller.backup_parameters(self.current_camera.device_path)
            if success:
                messagebox.showinfo("Success", "Parameters backed up successfully")
                self.status_var.set("Parameters backed up")
            else:
                messagebox.showerror("Error", "Failed to backup parameters")
                
        except Exception as e:
            logger.error(f"Failed to backup parameters: {e}")
            messagebox.showerror("Error", f"Failed to backup parameters: {e}")
    
    def restore_parameters(self):
        """Restore original camera parameters"""
        if not self.current_camera:
            messagebox.showwarning("Warning", "No camera selected")
            return
        
        try:
            success = self.camera_controller.restore_parameters(self.current_camera.device_path)
            if success:
                messagebox.showinfo("Success", "Parameters restored successfully")
                self.parameter_frame.refresh_parameters()
                self.status_var.set("Parameters restored")
            else:
                messagebox.showerror("Error", "Failed to restore parameters")
                
        except Exception as e:
            logger.error(f"Failed to restore parameters: {e}")
            messagebox.showerror("Error", f"Failed to restore parameters: {e}")
    
    def save_config(self):
        """Save current configuration"""
        if not self.current_camera:
            messagebox.showwarning("Warning", "No camera selected")
            return
        
        try:
            self.config_manager.save_camera_config(self.current_camera)
            messagebox.showinfo("Success", "Configuration saved successfully")
            self.status_var.set("Configuration saved")
            
        except Exception as e:
            logger.error(f"Failed to save configuration: {e}")
            messagebox.showerror("Error", f"Failed to save configuration: {e}")
    
    def load_config(self):
        """Load configuration from file"""
        try:
            file_path = filedialog.askopenfilename(
                title="Load Configuration",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )
            
            if file_path:
                # Implementation would load and apply configuration
                messagebox.showinfo("Info", "Load configuration feature coming soon")
                
        except Exception as e:
            logger.error(f"Failed to load configuration: {e}")
            messagebox.showerror("Error", f"Failed to load configuration: {e}")
    
    def load_saved_configs(self):
        """Load saved configurations for all cameras"""
        try:
            self.config_manager.load_all_configs()
            logger.info("Loaded saved configurations")
            
        except Exception as e:
            logger.warning(f"Failed to load saved configurations: {e}")
    
    def load_camera_config(self):
        """Load saved configuration for current camera"""
        if not self.current_camera:
            return
        
        try:
            config = self.config_manager.get_camera_config(self.current_camera.device_path)
            if config and isinstance(config, dict):
                # Apply configuration to camera
                parameters = config.get('parameters', {})
                if isinstance(parameters, dict):
                    for param_name, param_data in parameters.items():
                        if param_name in self.current_camera.parameters:
                            if isinstance(param_data, dict):
                                value = param_data.get('value')
                                if value is not None:
                                    self.camera_controller.set_parameter(
                                        self.current_camera.device_path,
                                        param_name,
                                        value
                                    )
                
                # Refresh parameter display
                self.parameter_frame.refresh_parameters()
                self.status_var.set("Configuration loaded")
                
        except Exception as e:
            import traceback
            logger.warning(f"Failed to load camera configuration: {e}\n{traceback.format_exc()}")
    
    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo(
            "About CamLoader",
            "CamLoader v1.1.0\\n\\n"
            "A GUI application for controlling V4L2 camera parameters.\\n\\n"
            "Features:\\n"
            "• Camera detection and selection\\n"
            "• Parameter control with live preview\\n"
            "• Configuration save/load\\n"
            "• Parameter backup/restore\\n"
            "• Startup configuration management\\n"
            "• Parameter tooltips and descriptions"
        )
    
    def show_startup_config(self):
        """Show startup configuration window"""
        try:
            StartupConfigWindow(self.root, self.camera_controller, self.config_manager)
        except Exception as e:
            logger.error(f"Failed to open startup configuration: {e}")
            messagebox.showerror("Error", f"Failed to open startup configuration: {e}")
    
    def apply_startup_configurations(self):
        """Apply startup configurations on application start"""
        try:
            from pathlib import Path
            import json
            
            config_path = Path.home() / ".camloader" / "startup_config.json"
            if not config_path.exists():
                return
            
            with open(config_path, 'r') as f:
                startup_configs = json.load(f)
            
            applied_count = 0
            for device_path, config in startup_configs.items():
                if not config.get("enabled", False):
                    continue
                
                camera = self.camera_controller.get_camera(device_path)
                if not camera:
                    logger.warning(f"Startup config: Camera {device_path} not found")
                    continue
                
                success_count = 0
                total_count = 0
                
                for param_name, param_value in config.get("parameters", {}).items():
                    total_count += 1
                    if self.camera_controller.set_parameter(device_path, param_name, param_value):
                        success_count += 1
                
                if total_count > 0:
                    applied_count += 1
                    logger.info(f"Applied startup config for {camera.name}: {success_count}/{total_count} parameters")
            
            if applied_count > 0:
                self.status_var.set(f"Applied startup configurations for {applied_count} cameras")
                
        except Exception as e:
            logger.warning(f"Failed to apply startup configurations: {e}")
    
    def on_closing(self):
        """Handle application closing"""
        try:
            # Stop preview
            self.preview_frame.stop_preview()
            
            # Save current configuration if camera is selected
            if self.current_camera:
                self.config_manager.save_camera_config(self.current_camera)
            
            # Close application
            self.root.destroy()
            
        except Exception as e:
            logger.error(f"Error during application shutdown: {e}")
            self.root.destroy()
    
    def run(self):
        """Run the application"""
        logger.info("Starting CamLoader GUI")
        self.root.mainloop()