"""
Configuration Manager
Handles saving and loading of camera configurations
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime

from camera.controller import CameraDevice, V4L2Parameter

logger = logging.getLogger(__name__)

class ConfigManager:
    """Manager for camera configuration persistence"""
    
    def __init__(self, config_dir: str = None):
        if config_dir:
            self.config_dir = Path(config_dir)
        else:
            # Default to data directory in project
            self.config_dir = Path(__file__).parent.parent.parent / "data" / "configs"
        
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        # Cache for loaded configurations
        self.configs: Dict[str, Dict] = {}
        
        logger.info(f"ConfigManager initialized with directory: {self.config_dir}")
    
    def _get_config_file_path(self, device_path: str) -> Path:
        """Get configuration file path for a device"""
        # Sanitize device path for filename
        filename = device_path.replace("/", "_").replace(" ", "_") + ".json"
        return self.config_dir / filename
    
    def _get_backup_file_path(self, device_path: str) -> Path:
        """Get backup file path for a device"""
        # Sanitize device path for filename
        filename = device_path.replace("/", "_").replace(" ", "_") + "_backup.json"
        return self.config_dir / filename
    
    def save_camera_config(self, camera: CameraDevice, include_backup: bool = True) -> bool:
        """Save camera configuration to file"""
        try:
            config_file = self._get_config_file_path(camera.device_path)
            
            # Build configuration data
            config_data = {
                "device_path": camera.device_path,
                "device_name": camera.name,
                "saved_at": datetime.now().isoformat(),
                "parameters": {}
            }
            
            # Add parameter data
            for param_name, param in camera.parameters.items():
                config_data["parameters"][param_name] = param.to_dict()
            
            # Save to file
            with open(config_file, 'w') as f:
                json.dump(config_data, f, indent=2)
            
            # Update cache
            self.configs[camera.device_path] = config_data
            
            logger.info(f"Saved configuration for {camera.name} to {config_file}")
            
            # Save backup if requested
            if include_backup:
                self.save_parameter_backup(camera)
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to save configuration for {camera.name}: {e}")
            return False
    
    def load_camera_config(self, device_path: str) -> Optional[Dict]:
        """Load camera configuration from file"""
        try:
            config_file = self._get_config_file_path(device_path)
            
            if not config_file.exists():
                logger.info(f"No configuration file found for {device_path}")
                return None
            
            with open(config_file, 'r') as f:
                config_data = json.load(f)
            
            # Update cache
            self.configs[device_path] = config_data
            
            logger.info(f"Loaded configuration for {device_path}")
            return config_data
            
        except Exception as e:
            logger.error(f"Failed to load configuration for {device_path}: {e}")
            return None
    
    def get_camera_config(self, device_path: str) -> Optional[Dict]:
        """Get camera configuration from cache or load from file"""
        if device_path in self.configs:
            return self.configs[device_path]
        
        return self.load_camera_config(device_path)
    
    def save_parameter_backup(self, camera: CameraDevice) -> bool:
        """Save original parameter values as backup"""
        try:
            backup_file = self._get_backup_file_path(camera.device_path)
            
            # Build backup data
            backup_data = {
                "device_path": camera.device_path,
                "device_name": camera.name,
                "backed_up_at": datetime.now().isoformat(),
                "original_parameters": {}
            }
            
            # Add original parameter values
            for param_name, param in camera.parameters.items():
                backup_data["original_parameters"][param_name] = {
                    "name": param.name,
                    "original_value": param.original_value,
                    "param_type": param.param_type
                }
            
            # Save to file
            with open(backup_file, 'w') as f:
                json.dump(backup_data, f, indent=2)
            
            logger.info(f"Saved parameter backup for {camera.name} to {backup_file}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save parameter backup for {camera.name}: {e}")
            return False
    
    def load_parameter_backup(self, device_path: str) -> Optional[Dict]:
        """Load parameter backup from file"""
        try:
            backup_file = self._get_backup_file_path(device_path)
            
            if not backup_file.exists():
                logger.info(f"No backup file found for {device_path}")
                return None
            
            with open(backup_file, 'r') as f:
                backup_data = json.load(f)
            
            logger.info(f"Loaded parameter backup for {device_path}")
            return backup_data
            
        except Exception as e:
            logger.error(f"Failed to load parameter backup for {device_path}: {e}")
            return None
    
    def list_saved_configs(self) -> List[Dict]:
        """List all saved configurations"""
        configs = []
        
        try:
            for config_file in self.config_dir.glob("*.json"):
                if config_file.name.endswith("_backup.json"):
                    continue  # Skip backup files
                
                try:
                    with open(config_file, 'r') as f:
                        config_data = json.load(f)
                    
                    configs.append({
                        "file_path": str(config_file),
                        "device_path": config_data.get("device_path"),
                        "device_name": config_data.get("device_name"),
                        "saved_at": config_data.get("saved_at")
                    })
                    
                except Exception as e:
                    logger.warning(f"Failed to read config file {config_file}: {e}")
            
        except Exception as e:
            logger.error(f"Failed to list configurations: {e}")
        
        return configs
    
    def delete_camera_config(self, device_path: str) -> bool:
        """Delete configuration for a camera"""
        try:
            config_file = self._get_config_file_path(device_path)
            backup_file = self._get_backup_file_path(device_path)
            
            deleted = False
            
            if config_file.exists():
                config_file.unlink()
                deleted = True
                logger.info(f"Deleted configuration file: {config_file}")
            
            if backup_file.exists():
                backup_file.unlink()
                deleted = True
                logger.info(f"Deleted backup file: {backup_file}")
            
            # Remove from cache
            if device_path in self.configs:
                del self.configs[device_path]
            
            return deleted
            
        except Exception as e:
            logger.error(f"Failed to delete configuration for {device_path}: {e}")
            return False
    
    def load_all_configs(self):
        """Load all available configurations into cache"""
        try:
            for config_file in self.config_dir.glob("*.json"):
                if config_file.name.endswith("_backup.json"):
                    continue  # Skip backup files
                
                try:
                    with open(config_file, 'r') as f:
                        config_data = json.load(f)
                    
                    device_path = config_data.get("device_path")
                    if device_path:
                        self.configs[device_path] = config_data
                    
                except Exception as e:
                    logger.warning(f"Failed to load config file {config_file}: {e}")
            
            logger.info(f"Loaded {len(self.configs)} configurations into cache")
            
        except Exception as e:
            logger.error(f"Failed to load all configurations: {e}")
    
    def export_config(self, device_path: str, export_path: str) -> bool:
        """Export configuration to specified path"""
        try:
            config = self.get_camera_config(device_path)
            if not config:
                logger.error(f"No configuration found for {device_path}")
                return False
            
            export_file = Path(export_path)
            export_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(export_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            logger.info(f"Exported configuration to {export_file}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to export configuration: {e}")
            return False
    
    def import_config(self, import_path: str, device_path: str = None) -> bool:
        """Import configuration from specified path"""
        try:
            import_file = Path(import_path)
            
            if not import_file.exists():
                logger.error(f"Import file not found: {import_file}")
                return False
            
            with open(import_file, 'r') as f:
                config_data = json.load(f)
            
            # Use provided device path or the one from config
            target_device = device_path or config_data.get("device_path")
            if not target_device:
                logger.error("No device path specified for import")
                return False
            
            # Update device path in config
            config_data["device_path"] = target_device
            config_data["imported_at"] = datetime.now().isoformat()
            
            # Save to configuration directory
            config_file = self._get_config_file_path(target_device)
            with open(config_file, 'w') as f:
                json.dump(config_data, f, indent=2)
            
            # Update cache
            self.configs[target_device] = config_data
            
            logger.info(f"Imported configuration from {import_file} for {target_device}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to import configuration: {e}")
            return False