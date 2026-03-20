#!/usr/bin/env python3
"""
CamLoader - Main Entry Point
A GUI application for controlling V4L2 camera parameters
"""

import sys
import os
import logging
import argparse
from pathlib import Path

# Fix PyInstaller LD_LIBRARY_PATH conflict BEFORE any other imports.
# PyInstaller sets LD_LIBRARY_PATH to its temp dir which contains bundled
# libraries (e.g. libstdc++.so.6) that are older than what system components
# like X11, Mesa, and v4l2-ctl require. Restoring the original value prevents
# segfaults in tkinter/X11 and failures in subprocess calls.
if hasattr(sys, '_MEIPASS'):
    _orig = os.environ.get('LD_LIBRARY_PATH_ORIG')
    if _orig is not None:
        os.environ['LD_LIBRARY_PATH'] = _orig
    elif 'LD_LIBRARY_PATH' in os.environ:
        del os.environ['LD_LIBRARY_PATH']

# Application version
__version__ = "0.0.0.30"

# Add src directory to Python path
src_dir = Path(__file__).parent
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from gui.main_window import CamLoaderMainWindow
from utils.logger import setup_logging

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='CamLoader - V4L2 Camera Controller',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s              # Start normally
  %(prog)s --minimized  # Start minimized to tray/taskbar
  %(prog)s --version    # Show version information
        '''
    )
    
    parser.add_argument(
        '--minimized', '-m',
        action='store_true',
        help='Start application minimized'
    )
    
    parser.add_argument(
        '--version', '-v',
        action='version',
        version=f'CamLoader v{__version__}'
    )
    
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug logging'
    )
    
    return parser.parse_args()

def main():
    """Main entry point for the application"""
    # Parse command line arguments
    args = parse_arguments()
    
    # Setup logging
    log_level = logging.DEBUG if args.debug else logging.INFO
    setup_logging(level=log_level)
    logger = logging.getLogger(__name__)
    
    try:
        logger.info(f"Starting CamLoader v{__version__}...")
        
        # Create and run the main application
        app = CamLoaderMainWindow(start_minimized=args.minimized, version=__version__)
        app.run()
        
    except Exception as e:
        logger.error(f"Failed to start application: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()