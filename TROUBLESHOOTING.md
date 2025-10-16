# CamLoader Troubleshooting Guide

## Executable Does Not Start on Debian/Ubuntu

### Common Problems and Solutions

#### 1. Check Permissions
```bash
# Set executable permission
chmod +x camloader-linux-x86_64

# Verify permissions
ls -la camloader-linux-x86_64
```

#### 2. Missing System Libraries
```bash
# Install required packages on Debian/Ubuntu:
sudo apt update
sudo apt install -y python3-tk python3-pil python3-pil.imagetk v4l-utils

# For older systems additionally:
sudo apt install -y libgtk-3-0 libgdk-pixbuf2.0-0 libfontconfig1 libxrender1 libxinerama1 libxi6 libxrandr2 libxcursor1 libxcomposite1 libxdamage1 libxfixes3 libxss1 libxtst6 libasound2

# OpenCV dependencies:
sudo apt install -y libopencv-dev python3-opencv
```

#### 3. Gather Debug Information

**Option A: Use Debug Wrapper**
```bash
# Download and use debug wrapper
wget https://github.com/Peschi90/cam-loader-linux/releases/latest/download/camloader-debug.sh
chmod +x camloader-debug.sh
./camloader-debug.sh
```

**Option B: Manual Debugging**
```bash
# Check file type
file camloader-linux-x86_64

# Check library dependencies
ldd camloader-linux-x86_64

# Start with error output
./camloader-linux-x86_64 2>&1 | tee camloader-error.log
```

#### 4. System Compatibility

**Minimum Requirements:**
- Linux x86_64 (64-bit)
- GLIBC >= 2.17 (Ubuntu 14.04+, Debian 8+)
- X11 (GUI environment)
- Python 3.7+ compatible libraries

**Compatibility Check:**
```bash
# Check GLIBC version
ldd --version

# X11 available?
echo $DISPLAY
xdpyinfo 2>/dev/null && echo "X11 OK" || echo "X11 Problem"

# V4L2 devices available?
ls /dev/video* 2>/dev/null || echo "No cameras found"
```

#### 5. Alternative: Python Environment

If the executable doesn't work, you can run the program directly with Python:

```bash
# Clone repository
git clone https://github.com/Peschi90/cam-loader-linux.git
cd cam-loader-linux

# Install dependencies
pip3 install -r requirements.txt

# Start program
python3 src/main.py
```

### Error Messages and Their Meaning

| Error Message | Cause | Solution |
|---------------|-------|----------|
| `./camloader-linux-x86_64: No such file or directory` | 32-bit system or missing libraries | Install GLIBC and dependencies |
| `ImportError: No module named '_tkinter'` | Tkinter not available | `sudo apt install python3-tk` |
| `cv2.error: OpenCV(4.x)` | OpenCV problem | `sudo apt install python3-opencv` |
| `Permission denied` | No execute permission | `chmod +x camloader-linux-x86_64` |
| Black window without content | GUI libraries missing | Install libgtk and X11 packages |

### Support

If problems persist:

1. Create debug log:
   ```bash
   ./camloader-debug.sh > debug-output.txt 2>&1
   ```

2. Create issue on GitHub with:
   - Debian/Ubuntu version (`lsb_release -a`)
   - Architecture (`uname -m`)
   - Debug log content
   - Error message

3. Link: https://github.com/Peschi90/cam-loader-linux/issues
