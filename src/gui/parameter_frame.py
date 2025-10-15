"""
Parameter Control Frame
GUI frame for displaying and controlling camera parameters
"""

import tkinter as tk
from tkinter import ttk
import logging
from typing import Optional, Callable

from camera.controller import CameraDevice, V4L2Parameter

logger = logging.getLogger(__name__)

class ParameterFrame(ttk.LabelFrame):
    """Frame for displaying and controlling camera parameters"""
    
    def __init__(self, parent, parameter_changed_callback: Callable[[str, any], None]):
        super().__init__(parent, text="Camera Parameters", padding="10")
        
        self.parameter_changed_callback = parameter_changed_callback
        self.camera: Optional[CameraDevice] = None
        self.parameter_widgets = {}
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the parameter control interface"""
        # Create scrollable frame
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        # Configure scrolling
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Pack scrollable components
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel
        self.bind_mouse_wheel()
    
    def bind_mouse_wheel(self):
        """Bind mouse wheel to canvas"""
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def _bind_to_mousewheel(event):
            self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        def _unbind_from_mousewheel(event):
            self.canvas.unbind_all("<MouseWheel>")
        
        self.canvas.bind('<Enter>', _bind_to_mousewheel)
        self.canvas.bind('<Leave>', _unbind_from_mousewheel)
    
    def set_camera(self, camera: CameraDevice):
        """Set the camera and display its parameters"""
        self.camera = camera
        self.create_parameter_controls()
    
    def create_parameter_controls(self):
        """Create controls for all camera parameters"""
        # Clear existing widgets
        self.clear_parameters()
        
        if not self.camera or not self.camera.parameters:
            no_params_label = ttk.Label(
                self.scrollable_frame, 
                text="No parameters available",
                font=("Arial", 10, "italic")
            )
            no_params_label.pack(pady=20)
            return
        
        # Create controls for each parameter
        row = 0
        for param_name, param in sorted(self.camera.parameters.items()):
            self.create_parameter_control(param, row)
            row += 1
    
    def create_parameter_control(self, param: V4L2Parameter, row: int):
        """Create control widget for a single parameter"""
        frame = ttk.Frame(self.scrollable_frame)
        frame.pack(fill="x", pady=2)
        
        # Parameter name label
        name_label = ttk.Label(frame, text=param.name, width=15)
        name_label.pack(side="left", padx=(0, 10))
        
        # Value display
        value_var = tk.StringVar(value=str(param.value))
        value_label = ttk.Label(frame, textvariable=value_var, width=8)
        value_label.pack(side="right", padx=(10, 0))
        
        # Create appropriate control widget
        if param.param_type == "bool":
            control = self.create_boolean_control(frame, param, value_var)
        elif param.min_val is not None and param.max_val is not None:
            control = self.create_scale_control(frame, param, value_var)
        else:
            control = self.create_entry_control(frame, param, value_var)
        
        # Store references
        self.parameter_widgets[param.name] = {
            'frame': frame,
            'control': control,
            'value_var': value_var,
            'param': param
        }
    
    def create_scale_control(self, parent, param: V4L2Parameter, value_var: tk.StringVar):
        """Create scale control for numeric parameters"""
        def on_scale_change(value):
            int_value = int(float(value))
            value_var.set(str(int_value))
            self.parameter_changed_callback(param.name, int_value)
        
        scale = ttk.Scale(
            parent,
            from_=param.min_val,
            to=param.max_val,
            orient="horizontal",
            command=on_scale_change,
            length=200
        )
        scale.set(param.value)
        scale.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        return scale
    
    def create_boolean_control(self, parent, param: V4L2Parameter, value_var: tk.StringVar):
        """Create checkbox control for boolean parameters"""
        def on_check_change():
            new_value = 1 if bool_var.get() else 0
            value_var.set(str(new_value))
            self.parameter_changed_callback(param.name, new_value)
        
        bool_var = tk.BooleanVar(value=bool(param.value))
        checkbox = ttk.Checkbutton(
            parent,
            variable=bool_var,
            command=on_check_change
        )
        checkbox.pack(side="left", padx=(0, 10))
        
        return checkbox
    
    def create_entry_control(self, parent, param: V4L2Parameter, value_var: tk.StringVar):
        """Create entry control for other parameters"""
        def on_entry_change(event=None):
            try:
                new_value = int(value_var.get())
                self.parameter_changed_callback(param.name, new_value)
            except ValueError:
                # Reset to current value if invalid input
                value_var.set(str(param.value))
        
        entry = ttk.Entry(parent, textvariable=value_var, width=10)
        entry.bind("<Return>", on_entry_change)
        entry.bind("<FocusOut>", on_entry_change)
        entry.pack(side="left", padx=(0, 10))
        
        return entry
    
    def clear_parameters(self):
        """Clear all parameter controls"""
        for widget_info in self.parameter_widgets.values():
            widget_info['frame'].destroy()
        self.parameter_widgets.clear()
        
        # Clear any existing widgets in scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
    
    def refresh_parameters(self):
        """Refresh parameter values from camera"""
        if not self.camera:
            return
        
        for param_name, widget_info in self.parameter_widgets.items():
            param = widget_info['param']
            value_var = widget_info['value_var']
            control = widget_info['control']
            
            # Update value display
            value_var.set(str(param.value))
            
            # Update control widget
            if isinstance(control, ttk.Scale):
                control.set(param.value)
            elif isinstance(control, ttk.Checkbutton):
                # Get the associated BooleanVar and update it
                control.invoke() if bool(param.value) != control.instate(['selected']) else None