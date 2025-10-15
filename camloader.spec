# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller specification file for CamLoader
This creates a standalone executable for Linux distribution
"""

import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path.cwd() / 'src'
sys.path.insert(0, str(src_path))

block_cipher = None

# Define the analysis
a = Analysis(
    ['src/main.py'],  # Entry point
    pathex=[str(src_path)],  # Additional paths for Python modules
    binaries=[],  # Binary files to include
    datas=[
        ('data', 'data'),  # Include data directory
        ('README.md', '.'),  # Include documentation
        ('LICENSE', '.'),
        ('CHANGELOG.md', '.'),
    ],
    hiddenimports=[
        # Core Python modules
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'logging',
        'json',
        'threading',
        'subprocess',
        'pathlib',
        'datetime',
        'platform',
        're',
        'time',
        'typing',
        
        # Third-party modules
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
        'cv2',
        'psutil',
        
        # Application modules
        'camera',
        'camera.controller',
        'gui', 
        'gui.main_window',
        'gui.parameter_frame',
        'gui.preview_frame',
        'config',
        'config.manager',
        'utils',
        'utils.logger',
    ],
    hookspath=[],  # Additional hook directories
    hooksconfig={},  # Hook configuration
    runtime_hooks=[],  # Runtime hooks
    excludes=[
        # Exclude unnecessary modules to reduce size
        'matplotlib',
        'numpy.testing',
        'scipy',
        'pandas',
        'jupyter',
        'IPython',
        'notebook',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Create PYZ archive
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Create executable
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='camloader',
    debug=False,  # Set to True for debugging
    bootloader_ignore_signals=False,
    strip=False,  # Set to True to reduce size (may cause issues)
    upx=True,  # Compress with UPX if available
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # GUI application, no console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add path to .ico file if you have an icon
)