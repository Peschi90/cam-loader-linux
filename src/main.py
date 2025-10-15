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

# Application version
__version__ = "0.0.0.23"

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