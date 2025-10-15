#!/usr/bin/env python3
"""
Debug script to test imports and identify issues
"""

import sys
import os
from pathlib import Path

print("=== CamLoader Debug Information ===")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

# Add src directory to path
src_dir = Path(__file__).parent / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))
    print(f"Added to Python path: {src_dir}")

print("\n=== Testing imports ===")

# Test basic imports
try:
    import tkinter as tk
    print("✓ tkinter import successful")
except ImportError as e:
    print(f"✗ tkinter import failed: {e}")

try:
    import logging
    print("✓ logging import successful")
except ImportError as e:
    print(f"✗ logging import failed: {e}")

# Test optional imports
try:
    import cv2
    print("✓ opencv (cv2) import successful")
except ImportError as e:
    print(f"⚠ opencv (cv2) import failed: {e}")

try:
    from PIL import Image, ImageTk
    print("✓ PIL import successful")
except ImportError as e:
    print(f"⚠ PIL import failed: {e}")

# Test our modules
print("\n=== Testing application modules ===")

try:
    from utils.logger import setup_logging
    print("✓ utils.logger import successful")
except ImportError as e:
    print(f"✗ utils.logger import failed: {e}")

try:
    from camera.controller import CameraController
    print("✓ camera.controller import successful")
except ImportError as e:
    print(f"✗ camera.controller import failed: {e}")

try:
    from config.manager import ConfigManager
    print("✓ config.manager import successful")
except ImportError as e:
    print(f"✗ config.manager import failed: {e}")

try:
    from gui.parameter_frame import ParameterFrame
    print("✓ gui.parameter_frame import successful")
except ImportError as e:
    print(f"✗ gui.parameter_frame import failed: {e}")

try:
    from gui.preview_frame import PreviewFrame
    print("✓ gui.preview_frame import successful")
except ImportError as e:
    print(f"✗ gui.preview_frame import failed: {e}")

try:
    from gui.main_window import CamLoaderMainWindow
    print("✓ gui.main_window import successful")
except ImportError as e:
    print(f"✗ gui.main_window import failed: {e}")

print("\n=== Testing basic functionality ===")

try:
    setup_logging()
    print("✓ Logging setup successful")
except Exception as e:
    print(f"✗ Logging setup failed: {e}")

try:
    controller = CameraController()
    cameras = controller.get_cameras()
    print(f"✓ Camera controller created, found {len(cameras)} cameras")
    for camera in cameras:
        print(f"  - {camera}")
except Exception as e:
    print(f"✗ Camera controller failed: {e}")

try:
    config_manager = ConfigManager()
    print("✓ Config manager created")
except Exception as e:
    print(f"✗ Config manager failed: {e}")

print("\n=== Test completed ===")
print("If all core modules loaded successfully, try running the GUI...")

# Test GUI creation
try:
    print("\n=== Testing GUI creation ===")
    import tkinter as tk
    
    root = tk.Tk()
    root.title("Test Window")
    root.geometry("300x200")
    
    label = tk.Label(root, text="CamLoader Test\\n\\nIf you see this, tkinter works!\\n\\nClose this window to continue.")
    label.pack(expand=True)
    
    # Show window briefly
    root.after(3000, root.destroy)  # Auto-close after 3 seconds
    print("✓ Test window created - should appear briefly")
    
    # Don't start mainloop in debug mode
    # root.mainloop()
    
except Exception as e:
    print(f"✗ GUI test failed: {e}")

print("\nDebug script completed!")