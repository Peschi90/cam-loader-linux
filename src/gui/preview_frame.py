"""
Preview Frame
GUI frame for displaying live camera preview
"""

import tkinter as tk
from tkinter import ttk
import threading
import logging
import time
from typing import Optional

# Optional imports for different platforms
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False

try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

logger = logging.getLogger(__name__)

class PreviewFrame(ttk.LabelFrame):
    """Frame for displaying live camera preview"""
    
    def __init__(self, parent):
        super().__init__(parent, text="Live Preview", padding="10")
        
        self.camera_device: Optional[str] = None
        self.cap: Optional[cv2.VideoCapture] = None
        self.preview_running = False
        self.preview_thread: Optional[threading.Thread] = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the preview interface"""
        # Control frame
        control_frame = ttk.Frame(self)
        control_frame.pack(fill="x", pady=(0, 10))
        
        # Start/Stop buttons
        self.start_button = ttk.Button(
            control_frame, 
            text="Start Preview", 
            command=self.start_preview
        )
        self.start_button.pack(side="left", padx=(0, 5))
        
        self.stop_button = ttk.Button(
            control_frame, 
            text="Stop Preview", 
            command=self.stop_preview,
            state="disabled"
        )
        self.stop_button.pack(side="left", padx=(0, 5))
        
        # Resolution info
        self.resolution_var = tk.StringVar(value="No preview")
        resolution_label = ttk.Label(control_frame, textvariable=self.resolution_var)
        resolution_label.pack(side="right")
        
        # Preview area
        self.preview_frame = ttk.Frame(self, relief="sunken", borderwidth=2)
        self.preview_frame.pack(fill="both", expand=True)
        
        # Preview label
        self.preview_label = ttk.Label(
            self.preview_frame, 
            text="No preview available\\nClick 'Start Preview' to begin",
            anchor="center",
            font=("Arial", 12)
        )
        self.preview_label.pack(expand=True, fill="both")
    
    def set_camera(self, device_path: str):
        """Set the camera device for preview"""
        if self.preview_running:
            self.stop_preview()
        
        self.camera_device = device_path
        logger.info(f"Preview camera set to: {device_path}")
    
    def start_preview(self):
        """Start the camera preview"""
        if not CV2_AVAILABLE:
            self.preview_label.config(
                text="Preview not available\\nOpenCV (cv2) not installed\\nInstall with: pip install opencv-python"
            )
            logger.warning("Cannot start preview: OpenCV not available")
            return
            
        if not self.camera_device:
            logger.warning("No camera device set for preview")
            return
        
        if self.preview_running:
            return
        
        try:
            # Extract camera index from device path (e.g., /dev/video0 -> 0)
            if "/dev/video" in self.camera_device:
                camera_index = int(self.camera_device.split('video')[1])
            else:
                # Fallback for Windows testing
                camera_index = 0
            
            # Open camera
            self.cap = cv2.VideoCapture(camera_index)
            if not self.cap.isOpened():
                logger.error(f"Failed to open camera {self.camera_device}")
                self.preview_label.config(
                    text="Failed to open camera\\nCheck camera connection and permissions"
                )
                return
            
            # Set camera properties for better performance
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cap.set(cv2.CAP_PROP_FPS, 30)
            
            # Start preview thread
            self.preview_running = True
            self.preview_thread = threading.Thread(target=self._preview_loop, daemon=True)
            self.preview_thread.start()
            
            # Update button states
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
            
            logger.info(f"Started preview for {self.camera_device}")
            
        except Exception as e:
            logger.error(f"Failed to start preview: {e}")
            self.preview_running = False
            if self.cap:
                self.cap.release()
                self.cap = None
            self.preview_label.config(
                text=f"Preview error:\\n{str(e)}"
            )
    
    def stop_preview(self):
        """Stop the camera preview"""
        if not self.preview_running:
            return
        
        self.preview_running = False
        
        # Wait for thread to finish
        if self.preview_thread and self.preview_thread.is_alive():
            self.preview_thread.join(timeout=1.0)
        
        # Release camera
        if self.cap:
            self.cap.release()
            self.cap = None
        
        # Update UI
        self.preview_label.config(image="")
        self.preview_label.config(
            text="Preview stopped\\nClick 'Start Preview' to begin"
        )
        self.resolution_var.set("No preview")
        
        # Update button states
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        
        logger.info("Stopped camera preview")
    
    def _preview_loop(self):
        """Main preview loop running in separate thread"""
        if not CV2_AVAILABLE:
            return
            
        while self.preview_running and self.cap:
            try:
                ret, frame = self.cap.read()
                if not ret:
                    logger.warning("Failed to read frame from camera")
                    time.sleep(0.1)
                    continue
                
                # Get frame dimensions
                height, width = frame.shape[:2]
                
                # Resize frame to fit preview area
                preview_width = 400
                preview_height = int(height * preview_width / width)
                
                frame_resized = cv2.resize(frame, (preview_width, preview_height))
                
                # Convert BGR to RGB
                frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
                
                # Convert to PIL Image and then to PhotoImage
                if PIL_AVAILABLE:
                    pil_image = Image.fromarray(frame_rgb)
                    photo = ImageTk.PhotoImage(pil_image)
                    
                    # Update preview label in main thread
                    self.preview_label.after(0, self._update_preview, photo, width, height)
                else:
                    # Fallback without PIL
                    self.preview_label.after(0, self._update_preview_text, width, height)
                
                # Control frame rate
                time.sleep(1/30)  # ~30 FPS
                
            except Exception as e:
                logger.error(f"Error in preview loop: {e}")
                time.sleep(0.1)
    
    def _update_preview(self, photo, width, height):
        """Update preview image in main thread"""
        if self.preview_running:
            self.preview_label.config(image=photo, text="")
            self.preview_label.image = photo  # Keep a reference
            self.resolution_var.set(f"{width}x{height}")
    
    def _update_preview_text(self, width, height):
        """Update preview text when PIL is not available"""
        if self.preview_running:
            self.preview_label.config(text=f"Camera active\\n{width}x{height}\\n(Image display requires PIL)")
            self.resolution_var.set(f"{width}x{height}")
    
    def __del__(self):
        """Cleanup when object is destroyed"""
        self.stop_preview()