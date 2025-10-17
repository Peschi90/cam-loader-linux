# CamLoader Troubleshooting Guide

## Common Issues and Solutions

### 1. Executable Does Not Start

Check permissions and install required packages:
```bash
chmod +x CamLoader-linux-x86_64
sudo apt install -y python3-tk v4l-utils libopencv-dev
```

### 2. No Cameras Found

```bash
ls -l /dev/video*
sudo usermod -a -G video $USER
# Re-login required!
```

### 3. Preview Not Working

```bash
v4l2-ctl --device=/dev/video0 --list-formats-ext
```

### 4. Debug Mode

```bash
./CamLoader-linux-x86_64 --debug
```

## Getting Help

Report issues: https://github.com/Peschi90/cam-loader-linux/issues/new

## Documentation

- [README.md](README.md)
- [CHANGELOG.md](CHANGELOG.md)
- [GitHub Repository](https://github.com/Peschi90/cam-loader-linux)

## Support

- Star the repository
- Donate: https://paypal.me/i3ull3t
