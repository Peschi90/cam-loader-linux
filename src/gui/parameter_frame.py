"""
Parameter Control Frame
GUI frame for displaying and controlling camera parameters
"""

import tkinter as tk
from tkinter import ttk
import logging
from typing import Optional, Callable

from camera.controller import CameraDevice, V4L2Parameter
from utils.parameter_tooltips import get_parameter_tooltip

logger = logging.getLogger(__name__)

class ToolTip:
    """Simple tooltip implementation"""
    
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.on_enter)
        self.widget.bind("<Leave>", self.on_leave)
    
    def on_enter(self, event=None):
        self.show_tooltip()
    
    def on_leave(self, event=None):
        self.hide_tooltip()
    
    def show_tooltip(self):
        if self.tooltip_window or not self.text:
            return
        
        x, y, _, _ = self.widget.bbox("insert") if hasattr(self.widget, 'bbox') else (0, 0, 0, 0)
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        
        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        
        label = tk.Label(
            tw, 
            text=self.text, 
            justify='left',
            background="#ffffe0", 
            relief='solid', 
            borderwidth=1,
            font=("Arial", 9),
            wraplength=300
        )
        label.pack(ipadx=1)
    
    def hide_tooltip(self):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

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
        
        # Parameter name label with tooltip
        name_label = ttk.Label(frame, text=param.name, width=15)
        name_label.pack(side="left", padx=(0, 10))
        
        # Add tooltip to the parameter name
        tooltip_text = get_parameter_tooltip(param.name)
        ToolTip(name_label, tooltip_text)
        
        # Current value display (always shows actual value)
        value_var = tk.StringVar(value=str(param.value))
        
        # Create appropriate control widget
        if param.param_type == "bool":
            control = self.create_boolean_control(frame, param, value_var)
            # For boolean, no additional text entry needed
            value_label = ttk.Label(frame, textvariable=value_var, width=8)
            value_label.pack(side="right", padx=(10, 0))
            # Add tooltip to control
            ToolTip(control, tooltip_text)
        elif param.min_val is not None and param.max_val is not None:
            # Scale control with text entry
            control = self.create_scale_control(frame, param, value_var)
            # Add text entry field for direct input
            text_entry = self.create_text_entry(frame, param, value_var, control)
            # Add tooltips to controls
            ToolTip(control, tooltip_text)
            ToolTip(text_entry, f"{tooltip_text}\n\nRange: {param.min_val} - {param.max_val}")
        else:
            # Just text entry for parameters without min/max
            control = self.create_entry_control(frame, param, value_var)
            # Value display for entry-only controls
            value_label = ttk.Label(frame, textvariable=value_var, width=8)
            value_label.pack(side="right", padx=(10, 0))
            # Add tooltip to control
            ToolTip(control, tooltip_text)
        
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
            length=150  # Reduced to make room for text entry
        )
        scale.set(param.value)
        scale.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        return scale
    
    def create_text_entry(self, parent, param: V4L2Parameter, value_var: tk.StringVar, scale_control):
        """Create text entry field for direct value input alongside scale"""
        def on_text_change(event=None):
            try:
                new_value = int(text_var.get())
                # Validate range
                if param.min_val is not None and new_value < param.min_val:
                    new_value = param.min_val
                elif param.max_val is not None and new_value > param.max_val:
                    new_value = param.max_val
                
                # Update both scale and display
                scale_control.set(new_value)
                value_var.set(str(new_value))
                text_var.set(str(new_value))
                self.parameter_changed_callback(param.name, new_value)
                
            except ValueError:
                # Reset to current value if invalid input
                text_var.set(str(param.value))
        
        # Text variable for the entry field
        text_var = tk.StringVar(value=str(param.value))
        
        # Create entry field
        entry = ttk.Entry(parent, textvariable=text_var, width=6)
        entry.bind("<Return>", on_text_change)
        entry.bind("<FocusOut>", on_text_change)
        entry.pack(side="right", padx=(5, 0))
        
        # Store text_var reference for updates
        self.parameter_widgets[param.name + "_text_var"] = text_var
        
        return entry
    
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