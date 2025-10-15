"""
Logger Utilities
Setup and configuration for application logging
"""

import logging
import sys
from pathlib import Path

def setup_logging(log_level: str = "INFO", log_file: str = None, level: int = None):
    """Setup application logging
    
    Args:
        log_level: String log level (INFO, DEBUG, etc.) - deprecated, use level instead
        log_file: Optional file path for log output
        level: Integer log level (logging.INFO, logging.DEBUG, etc.)
    """
    
    # Use level parameter if provided, otherwise use log_level string
    if level is not None:
        log_level_int = level
    else:
        log_level_int = getattr(logging, log_level.upper())
    
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(log_level_int)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level_int)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (optional)
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    logger.info("Logging initialized")