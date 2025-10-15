#!/usr/bin/env python3
"""
CamLoader - Main Entry Point
A GUI application for controlling V4L2 camera parameters
"""

import sys
import os
import logging
from pathlib import Path

# Add src directory to Python path
src_dir = Path(__file__).parent
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from gui.main_window import CamLoaderMainWindow
from utils.logger import setup_logging

def main():
    """Main entry point for the application"""
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Starting CamLoader application...")
        
        # Create and run the main application
        app = CamLoaderMainWindow()
        app.run()
        
    except Exception as e:
        logger.error(f"Failed to start application: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()