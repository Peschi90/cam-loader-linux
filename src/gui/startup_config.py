"""
Startup Configuration Window
Allows users to configure which cameras start with which parameters
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import logging
from typing import Dict, List, Optional
from pathlib import Path

from camera.controller import CameraController, CameraDevice, V4L2Parameter
from config.manager import ConfigManager

logger = logging.getLogger(__name__)

class StartupConfigWindow:
    """Window for configuring startup camera parameters"""
    
    def __init__(self, parent, camera_controller: CameraController, config_manager: ConfigManager):
        self.parent = parent
        self.camera_controller = camera_controller
        self.config_manager = config_manager
        
        # Create window
        self.window = tk.Toplevel(parent)
        self.window.title("Startup Configuration")
        self.window.geometry("800x600")
        self.window.resizable(True, True)
        
        # Make window modal
        self.window.transient(parent)
        self.window.grab_set()
        
        # Startup configurations
        self.startup_configs: Dict[str, Dict] = {}
        
        self.setup_ui()
        self.load_startup_configs()
        
        # Center window
        self.center_window()
    
    def center_window(self):
        """Center the window on screen"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.pack(fill="both", expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="Startup Camera Configuration", 
            font=("Arial", 14, "bold")
        )
        title_label.pack(pady=(0, 10))
        
        # Description
        desc_label = ttk.Label(
            main_frame,
            text="Configure which cameras should be automatically configured with specific parameters when the application starts.",
            wraplength=750
        )
        desc_label.pack(pady=(0, 15))
        
        # Camera list frame
        self.create_camera_list_frame(main_frame)
        
        # Buttons frame
        self.create_buttons_frame(main_frame)
    
    def create_camera_list_frame(self, parent):
        """Create frame for camera configuration list"""
        list_frame = ttk.LabelFrame(parent, text="Camera Startup Configurations", padding="10")
        list_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        # Treeview for configurations
        columns = ("Camera", "Device", "Enabled", "Parameters")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)
        
        # Configure columns
        self.tree.heading("Camera", text="Camera Name")
        self.tree.heading("Device", text="Device Path")
        self.tree.heading("Enabled", text="Enabled")
        self.tree.heading("Parameters", text="Parameters Count")
        
        self.tree.column("Camera", width=200)
        self.tree.column("Device", width=120)
        self.tree.column("Enabled", width=80)
        self.tree.column("Parameters", width=120)
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack treeview and scrollbar
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind double-click to edit
        self.tree.bind("<Double-1>", self.on_camera_double_click)
        
        # Control buttons frame
        controls_frame = ttk.Frame(list_frame)
        controls_frame.pack(fill="x", pady=(10, 0))
        
        ttk.Button(controls_frame, text="Add Camera", command=self.add_camera_config).pack(side="left", padx=(0, 5))
        ttk.Button(controls_frame, text="Edit Selected", command=self.edit_selected_config).pack(side="left", padx=(0, 5))
        ttk.Button(controls_frame, text="Remove Selected", command=self.remove_selected_config).pack(side="left", padx=(0, 5))
        ttk.Button(controls_frame, text="Refresh Cameras", command=self.refresh_cameras).pack(side="left", padx=(10, 0))
    
    def create_buttons_frame(self, parent):
        """Create frame for action buttons"""
        buttons_frame = ttk.Frame(parent)
        buttons_frame.pack(fill="x")
        
        ttk.Button(buttons_frame, text="Save & Close", command=self.save_and_close).pack(side="right", padx=(5, 0))
        ttk.Button(buttons_frame, text="Cancel", command=self.cancel).pack(side="right", padx=(5, 0))
        ttk.Button(buttons_frame, text="Apply", command=self.apply_configs).pack(side="right", padx=(5, 0))
        ttk.Button(buttons_frame, text="Test Selected", command=self.test_selected_config).pack(side="left")
    
    def refresh_cameras(self):
        """Refresh available cameras"""
        try:
            self.camera_controller = CameraController()
            self.populate_camera_list()
            messagebox.showinfo("Success", "Camera list refreshed")
        except Exception as e:
            logger.error(f"Failed to refresh cameras: {e}")
            messagebox.showerror("Error", f"Failed to refresh cameras: {e}")
    
    def populate_camera_list(self):
        """Populate the camera configuration list"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get available cameras
        cameras = self.camera_controller.get_cameras()
        
        for camera in cameras:
            config = self.startup_configs.get(camera.device_path, {})
            enabled = config.get("enabled", False)
            param_count = len(config.get("parameters", {}))
            
            # Add availability indicator
            camera_name = camera.name
            if not camera.is_available:
                camera_name += " (No Preview)"
            
            self.tree.insert("", "end", values=(
                camera_name,
                camera.device_path,
                "Yes" if enabled else "No",
                param_count
            ))
    
    def on_camera_double_click(self, event):
        """Handle double-click on camera item"""
        self.edit_selected_config()
    
    def add_camera_config(self):
        """Add new camera configuration"""
        cameras = self.camera_controller.get_cameras()
        if not cameras:
            messagebox.showwarning("Warning", "No cameras available")
            return
        
        # Show camera selection dialog
        self.show_camera_config_dialog()
    
    def edit_selected_config(self):
        """Edit selected camera configuration"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a camera to edit")
            return
        
        item = self.tree.item(selection[0])
        device_path = item["values"][1]
        
        # Find camera
        camera = self.camera_controller.get_camera(device_path)
        if not camera:
            messagebox.showerror("Error", "Camera not found")
            return
        
        self.show_camera_config_dialog(camera)
    
    def remove_selected_config(self):
        """Remove selected camera configuration"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a camera to remove")
            return
        
        item = self.tree.item(selection[0])
        device_path = item["values"][1]
        camera_name = item["values"][0]
        
        if messagebox.askyesno("Confirm", f"Remove startup configuration for {camera_name}?"):
            if device_path in self.startup_configs:
                del self.startup_configs[device_path]
            self.populate_camera_list()
    
    def show_camera_config_dialog(self, camera: Optional[CameraDevice] = None):
        """Show camera configuration dialog"""
        dialog = CameraConfigDialog(self.window, self.camera_controller, camera, self.startup_configs)
        self.window.wait_window(dialog.window)
        
        # Refresh list if configuration was updated
        if dialog.result:
            device_path, config = dialog.result
            self.startup_configs[device_path] = config
            self.populate_camera_list()
    
    def test_selected_config(self):
        """Test selected camera configuration"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a camera to test")
            return
        
        item = self.tree.item(selection[0])
        device_path = item["values"][1]
        
        if device_path not in self.startup_configs:
            messagebox.showwarning("Warning", "No configuration found for selected camera")
            return
        
        config = self.startup_configs[device_path]
        if not config.get("enabled", False):
            messagebox.showinfo("Info", "Configuration is disabled")
            return
        
        try:
            # Apply configuration
            camera = self.camera_controller.get_camera(device_path)
            if not camera:
                messagebox.showerror("Error", "Camera not found")
                return
            
            success_count = 0
            total_count = 0
            
            for param_name, param_value in config.get("parameters", {}).items():
                total_count += 1
                if self.camera_controller.set_parameter(device_path, param_name, param_value):
                    success_count += 1
            
            messagebox.showinfo(
                "Test Result", 
                f"Applied {success_count}/{total_count} parameters successfully"
            )
            
        except Exception as e:
            logger.error(f"Failed to test configuration: {e}")
            messagebox.showerror("Error", f"Failed to test configuration: {e}")
    
    def apply_configs(self):
        """Apply current configurations"""
        try:
            self.save_startup_configs()
            messagebox.showinfo("Success", "Startup configurations applied")
        except Exception as e:
            logger.error(f"Failed to apply configurations: {e}")
            messagebox.showerror("Error", f"Failed to apply configurations: {e}")
    
    def save_and_close(self):
        """Save configurations and close window"""
        try:
            self.save_startup_configs()
            self.window.destroy()
        except Exception as e:
            logger.error(f"Failed to save configurations: {e}")
            messagebox.showerror("Error", f"Failed to save configurations: {e}")
    
    def cancel(self):
        """Cancel and close window"""
        self.window.destroy()
    
    def load_startup_configs(self):
        """Load startup configurations from file"""
        try:
            config_path = Path.home() / ".camloader" / "startup_config.json"
            if config_path.exists():
                with open(config_path, 'r') as f:
                    self.startup_configs = json.load(f)
                logger.info("Loaded startup configurations")
            self.populate_camera_list()
        except Exception as e:
            logger.warning(f"Failed to load startup configurations: {e}")
            self.populate_camera_list()
    
    def save_startup_configs(self):
        """Save startup configurations to file"""
        try:
            config_path = Path.home() / ".camloader"
            config_path.mkdir(exist_ok=True)
            
            config_file = config_path / "startup_config.json"
            with open(config_file, 'w') as f:
                json.dump(self.startup_configs, f, indent=2)
            
            logger.info("Saved startup configurations")
        except Exception as e:
            logger.error(f"Failed to save startup configurations: {e}")
            raise

class CameraConfigDialog:
    """Dialog for configuring individual camera parameters"""
    
    def __init__(self, parent, camera_controller: CameraController, camera: Optional[CameraDevice], startup_configs: Dict):
        self.parent = parent
        self.camera_controller = camera_controller
        self.camera = camera
        self.startup_configs = startup_configs
        self.result = None
        
        # Create dialog window
        self.window = tk.Toplevel(parent)
        self.window.title("Camera Configuration")
        self.window.geometry("600x500")
        self.window.resizable(True, True)
        
        # Make window modal (after it's visible)
        self.window.transient(parent)
        
        # Parameter selections
        self.param_vars = {}
        self.param_values = {}
        
        self.setup_ui()
        
        # Center window
        self.center_window()
        
        # Set grab after window is fully created and visible
        self.window.after(100, self.set_modal)
    
    def set_modal(self):
        """Set modal grab after window is visible"""
        try:
            self.window.grab_set()
        except tk.TclError as e:
            logger.warning(f"Could not set modal grab: {e}")
    
    def center_window(self):
        """Center the window on parent"""
        self.window.update_idletasks()
        parent_x = self.parent.winfo_rootx()
        parent_y = self.parent.winfo_rooty()
        parent_width = self.parent.winfo_width()
        parent_height = self.parent.winfo_height()
        
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = parent_x + (parent_width // 2) - (width // 2)
        y = parent_y + (parent_height // 2) - (height // 2)
        
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_ui(self):
        """Setup the dialog UI"""
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.pack(fill="both", expand=True)
        
        # Camera selection if no camera provided
        if not self.camera:
            self.create_camera_selection(main_frame)
        else:
            self.create_parameter_selection(main_frame)
        
        # Buttons
        self.create_buttons(main_frame)
    
    def create_camera_selection(self, parent):
        """Create camera selection interface"""
        selection_frame = ttk.LabelFrame(parent, text="Select Camera", padding="10")
        selection_frame.pack(fill="x", pady=(0, 10))
        
        cameras = self.camera_controller.get_cameras()
        camera_names = [f"{cam.name} ({cam.device_path})" for cam in cameras]
        
        self.camera_var = tk.StringVar()
        camera_combo = ttk.Combobox(selection_frame, textvariable=self.camera_var, values=camera_names, state="readonly")
        camera_combo.pack(fill="x")
        camera_combo.bind("<<ComboboxSelected>>", self.on_camera_selected)
        
        if cameras:
            camera_combo.current(0)
            self.on_camera_selected()
    
    def on_camera_selected(self, event=None):
        """Handle camera selection"""
        if hasattr(self, 'param_frame'):
            self.param_frame.destroy()
        
        selection = self.camera_var.get()
        if not selection:
            return
        
        # Extract device path
        device_path = selection.split("(")[1].split(")")[0]
        self.camera = self.camera_controller.get_camera(device_path)
        
        if self.camera:
            self.create_parameter_selection(self.window.children['!frame'])
    
    def create_parameter_selection(self, parent):
        """Create parameter selection interface"""
        self.param_frame = ttk.LabelFrame(parent, text="Parameter Configuration", padding="10")
        self.param_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        # Enable checkbox
        self.enabled_var = tk.BooleanVar()
        if self.camera and self.camera.device_path in self.startup_configs:
            self.enabled_var.set(self.startup_configs[self.camera.device_path].get("enabled", False))
        
        enable_frame = ttk.Frame(self.param_frame)
        enable_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Checkbutton(
            enable_frame, 
            text="Enable startup configuration for this camera", 
            variable=self.enabled_var
        ).pack(side="left")
        
        # Parameters list with scrollbar
        canvas = tk.Canvas(self.param_frame)
        scrollbar = ttk.Scrollbar(self.param_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack components
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Create parameter controls
        if self.camera and self.camera.parameters:
            existing_config = {}
            if self.camera.device_path in self.startup_configs:
                existing_config = self.startup_configs[self.camera.device_path].get("parameters", {})
            
            for param_name, param in sorted(self.camera.parameters.items()):
                self.create_parameter_control(scrollable_frame, param, existing_config.get(param_name))
    
    def create_parameter_control(self, parent, param: V4L2Parameter, existing_value=None):
        """Create control for a single parameter"""
        frame = ttk.Frame(parent)
        frame.pack(fill="x", pady=2)
        
        # Checkbox to include parameter
        include_var = tk.BooleanVar(value=existing_value is not None)
        self.param_vars[param.name] = include_var
        
        checkbox = ttk.Checkbutton(frame, variable=include_var)
        checkbox.pack(side="left", padx=(0, 5))
        
        # Parameter name with current value info
        current_value = f" (current: {param.value})"
        name_text = f"{param.name}{current_value}"
        name_label = ttk.Label(frame, text=name_text, width=30)
        name_label.pack(side="left", padx=(0, 10))
        
        # Value control with better input options
        if param.param_type == "bool":
            value_var = tk.BooleanVar(value=bool(existing_value if existing_value is not None else param.value))
            control = ttk.Checkbutton(frame, variable=value_var, text="Enable")
        elif param.min_val is not None and param.max_val is not None:
            value_var = tk.IntVar(value=existing_value if existing_value is not None else param.value)
            
            # Create a frame for scale and entry
            control_frame = ttk.Frame(frame)
            control_frame.pack(side="left", padx=(0, 10))
            
            # Scale control
            scale = ttk.Scale(
                control_frame, 
                from_=param.min_val, 
                to=param.max_val, 
                variable=value_var,
                orient="horizontal",
                length=150
            )
            scale.pack(side="left", padx=(0, 5))
            
            # Text entry for precise input
            entry_var = tk.StringVar(value=str(value_var.get()))
            entry = ttk.Entry(control_frame, textvariable=entry_var, width=8)
            entry.pack(side="left")
            
            # Synchronize scale and entry
            def sync_scale_to_entry():
                try:
                    val = int(entry_var.get())
                    if param.min_val <= val <= param.max_val:
                        value_var.set(val)
                    else:
                        entry_var.set(str(value_var.get()))
                except ValueError:
                    entry_var.set(str(value_var.get()))
            
            def sync_entry_to_scale(*args):
                entry_var.set(str(value_var.get()))
            
            entry.bind('<Return>', lambda e: sync_scale_to_entry())
            entry.bind('<FocusOut>', lambda e: sync_scale_to_entry())
            value_var.trace('w', sync_entry_to_scale)
            
            # Range info
            range_label = ttk.Label(control_frame, text=f"({param.min_val}-{param.max_val})", font=("Arial", 8))
            range_label.pack(side="left", padx=(5, 0))
            
            control = control_frame
        else:
            value_var = tk.StringVar(value=str(existing_value if existing_value is not None else param.value))
            control = ttk.Entry(frame, textvariable=value_var, width=15)
        
        if param.param_type != "bool" and not (param.min_val is not None and param.max_val is not None):
            control.pack(side="left", padx=(0, 10))
            
        self.param_values[param.name] = value_var
        
        # Current value display
        current_label = ttk.Label(frame, text=f"Current: {param.value}")
        current_label.pack(side="left")
    
    def create_buttons(self, parent):
        """Create dialog buttons"""
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill="x")
        
        ttk.Button(button_frame, text="OK", command=self.ok_clicked).pack(side="right", padx=(5, 0))
        ttk.Button(button_frame, text="Cancel", command=self.cancel_clicked).pack(side="right")
    
    def ok_clicked(self):
        """Handle OK button click"""
        if not self.camera:
            messagebox.showwarning("Warning", "Please select a camera")
            return
        
        # Collect configuration
        config = {
            "enabled": self.enabled_var.get(),
            "parameters": {}
        }
        
        for param_name, include_var in self.param_vars.items():
            if include_var.get():
                value_var = self.param_values[param_name]
                config["parameters"][param_name] = value_var.get()
        
        self.result = (self.camera.device_path, config)
        self.window.destroy()
    
    def cancel_clicked(self):
        """Handle Cancel button click"""
        self.result = None
        self.window.destroy()