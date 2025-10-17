# CamLoader - V4L2 Camera Parameter Controller

A user-friendly GUI application for controlling V4L2 camera parameters on Linux, developed as an alternative to guvcview with a focus on simplicity and maintainability.

## Features

### Main Functions
- **Camera Detection**: Automatic detection of all available V4L2 cameras
- **Parameter Control**: Intuitive controls for all camera parameters
- **Live Preview**: Real-time camera preview with configurable resolution
- **Configuration**: Save and load camera settings per camera
- **Backup System**: Automatic backup and restoration of original parameters
- **Multi-Camera**: Support for multiple connected cameras simultaneously
- **Startup Configuration**: Automatic loading of settings at program startup
- **Parameter Tooltips**: Helpful descriptions for all parameters
- **Lock Status**: Visualization of locked parameters
- **Detachable Preview**: Preview window can be detached
- **CLI Support**: Command line arguments (--minimized, --debug, --version)

### Technical Details
- **Programming Language**: Python 3.8+ (GLIBC 2.17+ compatible)
- **GUI Framework**: tkinter
- **V4L2 Integration**: Direct v4l2-ctl commands
- **Configuration**: JSON-based storage per camera
- **Build System**: GitHub Actions with PyInstaller
- **Release**: Standalone Linux x86_64 Executable

## Installation

### Precompiled Binary (recommended)

Download latest version:
```bash
wget https://github.com/Peschi90/cam-loader-linux/releases/latest/download/CamLoader-linux-x86_64
chmod +x CamLoader-linux-x86_64
./CamLoader-linux-x86_64
```

### System Requirements
- Linux with V4L2 support
- x86_64 architecture
- GLIBC 2.17 or higher
- v4l-utils installed

## Usage

### CLI Arguments
```bash
./CamLoader-linux-x86_64                # Start normally
./CamLoader-linux-x86_64 --minimized    # Start minimized
./CamLoader-linux-x86_64 --debug        # Debug logging
./CamLoader-linux-x86_64 --version      # Show version
```

## Documentation
- **CHANGELOG**: See [CHANGELOG.md](CHANGELOG.md)
- **TROUBLESHOOTING**: See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **GitHub**: [Peschi90/cam-loader-linux](https://github.com/Peschi90/cam-loader-linux)

## Support
- Report bugs: [GitHub Issues](https://github.com/Peschi90/cam-loader-linux/issues/new)
- Donate: [PayPal](https://paypal.me/i3ull3t)

## License
MIT License - see [LICENSE](LICENSE) file for details.

---
**CamLoader** - Simple V4L2 camera control for Linux
