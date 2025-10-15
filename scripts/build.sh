#!/bin/bash
# Build script for CamLoader Linux application

set -e  # Exit on any error

echo "=== CamLoader Build Script ==="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_NAME="camloader"
BUILD_DIR="build"
DIST_DIR="dist"
VENV_DIR="venv"

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    print_error "This script is designed for Linux systems only"
    exit 1
fi

# Check for required system dependencies
check_dependencies() {
    print_status "Checking system dependencies..."
    
    local missing_deps=()
    
    # Check for v4l-utils
    if ! command -v v4l2-ctl &> /dev/null; then
        missing_deps+=("v4l-utils")
    fi
    
    # Check for Python 3
    if ! command -v python3 &> /dev/null; then
        missing_deps+=("python3")
    fi
    
    # Check for pip
    if ! command -v pip3 &> /dev/null && ! python3 -m pip --version &> /dev/null; then
        missing_deps+=("python3-pip")
    fi
    
    # Check for tkinter
    if ! python3 -c "import tkinter" &> /dev/null; then
        missing_deps+=("python3-tkinter")
    fi
    
    if [ ${#missing_deps[@]} -ne 0 ]; then
        print_error "Missing required dependencies: ${missing_deps[*]}"
        print_status "Please install them using your package manager:"
        print_status "  Ubuntu/Debian: sudo apt install ${missing_deps[*]}"
        print_status "  Fedora: sudo dnf install ${missing_deps[*]}"
        print_status "  Arch: sudo pacman -S ${missing_deps[*]}"
        exit 1
    fi
    
    print_success "All system dependencies are available"
}

# Setup Python virtual environment
setup_venv() {
    print_status "Setting up Python virtual environment..."
    
    if [ -d "$VENV_DIR" ]; then
        print_warning "Virtual environment already exists, removing..."
        rm -rf "$VENV_DIR"
    fi
    
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    
    # Upgrade pip
    pip install --upgrade pip
    
    print_success "Virtual environment created"
}

# Install Python dependencies
install_dependencies() {
    print_status "Installing Python dependencies..."
    
    if [ ! -f "requirements.txt" ]; then
        print_error "requirements.txt not found"
        exit 1
    fi
    
    # Activate virtual environment
    source "$VENV_DIR/bin/activate"
    
    # Install requirements
    pip install -r requirements.txt
    
    print_success "Python dependencies installed"
}

# Build the application
build_app() {
    print_status "Building application..."
    
    # Activate virtual environment
    source "$VENV_DIR/bin/activate"
    
    # Clean previous builds
    rm -rf "$BUILD_DIR" "$DIST_DIR"
    
    # Build source distribution
    python setup.py sdist bdist_wheel
    
    print_success "Application built successfully"
}

# Create launcher script
create_launcher() {
    print_status "Creating launcher script..."
    
    local launcher_script="$DIST_DIR/camloader.sh"
    
    cat > "$launcher_script" << 'EOF'
#!/bin/bash
# CamLoader Launcher Script

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Activate virtual environment and run the application
cd "$PROJECT_DIR"
source venv/bin/activate
python src/main.py "$@"
EOF
    
    chmod +x "$launcher_script"
    
    print_success "Launcher script created: $launcher_script"
}

# Create desktop entry
create_desktop_entry() {
    print_status "Creating desktop entry..."
    
    local project_dir="$(pwd)"
    local desktop_file="$DIST_DIR/camloader.desktop"
    
    cat > "$desktop_file" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=CamLoader
Comment=V4L2 Camera Parameter Controller
Exec=$project_dir/dist/camloader.sh
Icon=$project_dir/data/icon.png
Terminal=false
Categories=AudioVideo;Video;Photography;
Keywords=camera;v4l2;video;parameters;
EOF
    
    print_success "Desktop entry created: $desktop_file"
    print_status "To install system-wide, copy to ~/.local/share/applications/ or /usr/share/applications/"
}

# Create installation package
create_package() {
    print_status "Creating installation package..."
    
    local package_dir="$DIST_DIR/camloader-package"
    local tarball="$DIST_DIR/camloader-1.0.0-linux.tar.gz"
    
    # Create package directory structure
    mkdir -p "$package_dir"
    
    # Copy application files
    cp -r src "$package_dir/"
    cp -r data "$package_dir/"
    cp requirements.txt "$package_dir/"
    cp setup.py "$package_dir/"
    cp README.md "$package_dir/" 2>/dev/null || true
    
    # Copy scripts
    cp "$DIST_DIR/camloader.sh" "$package_dir/"
    cp "$DIST_DIR/camloader.desktop" "$package_dir/"
    
    # Create install script
    cat > "$package_dir/install.sh" << 'EOF'
#!/bin/bash
# CamLoader Installation Script

set -e

echo "Installing CamLoader..."

# Check for Python 3 and required packages
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed"
    exit 1
fi

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "Installation completed successfully!"
echo "Run ./camloader.sh to start the application"
EOF
    
    chmod +x "$package_dir/install.sh"
    
    # Create tarball
    cd "$DIST_DIR"
    tar -czf "$(basename "$tarball")" "$(basename "$package_dir")"
    cd ..
    
    print_success "Installation package created: $tarball"
}

# Test the application
test_app() {
    print_status "Testing application..."
    
    # Activate virtual environment
    source "$VENV_DIR/bin/activate"
    
    # Run basic import test
    python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from main import main
    from camera.controller import CameraController
    from gui.main_window import CamLoaderMainWindow
    print('✓ All modules imported successfully')
except ImportError as e:
    print(f'✗ Import error: {e}')
    sys.exit(1)
"
    
    print_success "Application test passed"
}

# Main build process
main() {
    print_status "Starting build process for $PROJECT_NAME"
    
    # Parse command line arguments
    local skip_deps=false
    local skip_test=false
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            --skip-deps)
                skip_deps=true
                shift
                ;;
            --skip-test)
                skip_test=true
                shift
                ;;
            -h|--help)
                echo "Usage: $0 [OPTIONS]"
                echo "Options:"
                echo "  --skip-deps    Skip dependency installation"
                echo "  --skip-test    Skip application testing"
                echo "  -h, --help     Show this help message"
                exit 0
                ;;
            *)
                print_error "Unknown option: $1"
                exit 1
                ;;
        esac
    done
    
    # Check system dependencies
    check_dependencies
    
    # Setup build environment
    if [ "$skip_deps" = false ]; then
        setup_venv
        install_dependencies
    else
        print_warning "Skipping dependency installation"
    fi
    
    # Build application
    build_app
    
    # Test application
    if [ "$skip_test" = false ]; then
        test_app
    else
        print_warning "Skipping application test"
    fi
    
    # Create distribution files
    create_launcher
    create_desktop_entry
    create_package
    
    print_success "Build completed successfully!"
    print_status "Distribution files created in: $DIST_DIR"
    print_status "To run the application: ./dist/camloader.sh"
    print_status "To install desktop entry: cp dist/camloader.desktop ~/.local/share/applications/"
}

# Run main function
main "$@"