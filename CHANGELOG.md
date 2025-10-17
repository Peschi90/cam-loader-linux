# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Plugin system for extended parameters
- Scripting support for automation
- Extended preview options (histogram, etc.)
- Multi-language support
- Dark theme

## [0.0.0.26] - 2025-01-17

### Fixed
- **Documentation Corruption** - Removed all duplicate content from README, CHANGELOG, and TROUBLESHOOTING files
- **Clean File Structure** - All documentation files now have single, clean English-only content

## [0.0.0.25] - 2025-01-16

### Fixed
- **Mixed Language Content** - Removed all German text from documentation
- **Clean English Documentation** - All files now contain only English content

## [0.0.0.24] - 2025-01-16

### Changed
- **Documentation Translation** - Translated all documentation to English
- **International Accessibility** - Made project accessible to international developers

## [0.0.0.23] - 2025-01-16

### Added
- **Config Folder Access** - Added Open Config Folder button to About dialog
- **Menu Integration** - Added File → Open Config Folder menu option

## [0.0.0.22] - 2025-01-16

### Added
- **Donation Button** - Added PayPal donation button to About dialog

## [0.0.0.21] - 2025-01-16

### Added
- **GitHub Issue Integration** - New menu option Help → Report Issue

## [0.0.0.20] - 2025-01-16

### Fixed
- **Duplicate Parameter Application** - Fixed parameters applied twice during startup
- **--minimized Flag** - Fixed window showing when using --minimized argument

## [0.0.0.19] - 2025-01-16

### Added
- **Startup Configuration Improvements** - User-friendly dialog for setting startup parameters

## [0.0.0.18] - 2025-01-16

### Added
- **About Dialog** - New menu option Help → About with version information

## [0.0.0.17] - 2025-01-16

### Added
- **Detachable Preview Window** - Preview can be detached to separate window

## [0.0.0.16] - 2025-01-16

### Fixed
- **Parameter Lock Visualization** - Added visual feedback for locked parameters

## [0.0.0.15] - 2025-01-16

### Added
- **Enhanced Parameter Tooltips** - Descriptive tooltips for all camera parameters

## [0.0.0.14] - 2025-01-16

### Fixed
- **Startup Configuration Timing** - Fixed issue where startup config was applied too early

## [0.0.0.13] - 2025-01-16

### Added
- **Startup Configuration Feature** - Parameters automatically applied when camera is detected

## [0.0.0.12] - 2025-01-16

### Fixed
- **Preview Switching** - Fixed crash when switching cameras with running preview

## [0.0.0.11] - 2025-01-16

### Fixed
- **Parameter Synchronization** - All parameters correctly synchronized after loading config

## [0.0.0.10] - 2025-01-16

### Added
- **Command Line Arguments** - Added --minimized, --debug, --version flags

## [0.0.0.9] - 2025-01-16

### Fixed
- **Backup System** - Backup only created once per camera session

## [0.0.0.8] - 2025-01-16

### Added
- **GitHub Actions CI/CD** - Automated build process with PyInstaller

## [0.0.0.7] - 2025-01-16

### Added
- **GitHub Actions Workflow** for automated builds

## [0.0.0.6] - 2025-01-16

### Added
- **Backup and Restore Functionality** - Save and restore original camera parameters

## [0.0.0.5] - 2025-01-16

### Added
- **Configuration System** - Save and load camera parameters per camera

## [0.0.0.4] - 2025-01-16

### Added
- **Camera Detection System** - Automatic detection of all V4L2 cameras

## [0.0.0.3] - 2025-01-16

### Added
- **Live Camera Preview** - Real-time camera feed display

## [0.0.0.2] - 2025-01-16

### Added
- **Parameter Control Interface** - Dynamic slider generation for parameters

## [0.0.0.1] - 2025-01-16

### Added
- **Initial Project Structure** - Basic Python package structure with tkinter GUI
