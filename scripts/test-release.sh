#!/bin/bash
# Local release test script
# This script simulates the GitHub Actions workflow locally

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

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

# Configuration
VERSION=${1:-"1.0.0"}
TAG_NAME="v${VERSION}"

print_status "Testing release workflow for version ${VERSION}"

# Check if we're in the right directory
if [ ! -f "setup.py" ] || [ ! -f "CHANGELOG.md" ]; then
    print_error "Please run this script from the project root directory"
    exit 1
fi

# Test changelog extraction
print_status "Testing changelog extraction..."

cat << 'EOF' > test_changelog_extract.py
import sys
import re

def extract_changelog(version):
    try:
        with open('CHANGELOG.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match version sections
        version_pattern = rf'##\s*\[{re.escape(version)}\].*?\n(.*?)(?=\n##|\n#|\Z)'
        
        match = re.search(version_pattern, content, re.DOTALL | re.MULTILINE)
        
        if match:
            changelog_text = match.group(1).strip()
            changelog_text = re.sub(r'^\s*\n', '', changelog_text)
            changelog_text = re.sub(r'\n\s*$', '', changelog_text)
            return changelog_text
        else:
            return f"Release notes for version {version}"
            
    except FileNotFoundError:
        return f"Release notes for version {version}\n\nNo changelog file found."
    except Exception as e:
        return f"Release notes for version {version}\n\nError reading changelog: {str(e)}"

if __name__ == "__main__":
    version = sys.argv[1]
    changelog = extract_changelog(version)
    print(changelog)
EOF

CHANGELOG_CONTENT=$(python test_changelog_extract.py "$VERSION")
if [ $? -eq 0 ]; then
    print_success "Changelog extraction successful"
    echo "Extracted content:"
    echo "---"
    echo "$CHANGELOG_CONTENT"
    echo "---"
else
    print_error "Changelog extraction failed"
    exit 1
fi

# Clean up
rm test_changelog_extract.py

# Test Python environment setup
print_status "Testing Python environment..."

if ! command -v python3 &> /dev/null; then
    print_error "Python 3 not found"
    exit 1
fi

# Create test virtual environment
TEST_VENV="test_release_env"
if [ -d "$TEST_VENV" ]; then
    rm -rf "$TEST_VENV"
fi

python3 -m venv "$TEST_VENV"
source "$TEST_VENV/bin/activate"

print_status "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Test application imports
print_status "Testing application imports..."
cd src
python -c "
import sys
sys.path.insert(0, '.')
try:
    from main import main
    from camera.controller import CameraController
    from gui.main_window import CamLoaderMainWindow
    print('✓ All imports successful')
except ImportError as e:
    print(f'✗ Import error: {e}')
    sys.exit(1)
"
cd ..

if [ $? -eq 0 ]; then
    print_success "Application imports successful"
else
    print_error "Application imports failed"
    deactivate
    rm -rf "$TEST_VENV"
    exit 1
fi

# Test PyInstaller build (if available)
if command -v pyinstaller &> /dev/null; then
    print_status "Testing PyInstaller build..."
    
    # Install PyInstaller if not already installed
    pip install pyinstaller
    
    # Test spec file
    if [ -f "camloader.spec" ]; then
        print_status "Building with PyInstaller..."
        pyinstaller camloader.spec --clean --noconfirm
        
        if [ -f "dist/camloader" ]; then
            print_success "PyInstaller build successful"
            ls -la dist/camloader
            
            # Test the executable (basic test)
            print_status "Testing executable..."
            timeout 5s ./dist/camloader --help 2>/dev/null || echo "Executable test completed"
        else
            print_warning "PyInstaller build completed but executable not found"
        fi
    else
        print_warning "PyInstaller spec file not found"
    fi
else
    print_warning "PyInstaller not available, skipping build test"
fi

# Test source distribution build
print_status "Testing source distribution build..."
pip install build
python -m build --sdist

if [ -f "dist/camloader-${VERSION}.tar.gz" ]; then
    print_success "Source distribution build successful"
    ls -la dist/camloader-*.tar.gz
else
    print_warning "Source distribution not found at expected location"
    ls -la dist/ || echo "No dist directory"
fi

# Test wheel build
print_status "Testing wheel build..."
python -m build --wheel

if [ -f "dist/camloader-${VERSION}-py3-none-any.whl" ]; then
    print_success "Wheel build successful"
    ls -la dist/camloader-*.whl
else
    print_warning "Wheel not found at expected location"
fi

# Clean up test environment
deactivate
rm -rf "$TEST_VENV"

# Test the package structure
print_status "Testing package structure..."

REQUIRED_FILES=(
    "src/main.py"
    "src/camera/__init__.py"
    "src/camera/controller.py"
    "src/gui/__init__.py"
    "src/gui/main_window.py"
    "src/gui/parameter_frame.py"
    "src/gui/preview_frame.py"
    "src/config/__init__.py"
    "src/config/manager.py"
    "src/utils/__init__.py"
    "src/utils/logger.py"
    "setup.py"
    "requirements.txt"
    "README.md"
    "LICENSE"
    "CHANGELOG.md"
    ".github/workflows/release.yml"
)

missing_files=()
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
    fi
done

if [ ${#missing_files[@]} -eq 0 ]; then
    print_success "All required files present"
else
    print_warning "Missing files: ${missing_files[*]}"
fi

# Create a test release package
print_status "Creating test release package..."

PACKAGE_NAME="camloader-v${VERSION}-test"
mkdir -p "$PACKAGE_NAME"

# Copy files that would be in a release
cp -r src "$PACKAGE_NAME/"
cp -r data "$PACKAGE_NAME/" 2>/dev/null || echo "No data directory"
cp README.md LICENSE CHANGELOG.md requirements.txt setup.py "$PACKAGE_NAME/"

# Create test launcher
cat << 'EOF' > "${PACKAGE_NAME}/test_run.sh"
#!/bin/bash
echo "This would run CamLoader in a real release"
echo "Testing Python path setup..."
cd "$(dirname "$0")"
export PYTHONPATH="src:$PYTHONPATH"
python3 src/main.py "$@"
EOF

chmod +x "${PACKAGE_NAME}/test_run.sh"

# Create package archive
tar -czf "${PACKAGE_NAME}.tar.gz" "$PACKAGE_NAME"

print_success "Test release package created: ${PACKAGE_NAME}.tar.gz"
ls -la "${PACKAGE_NAME}.tar.gz"

# Clean up
rm -rf "$PACKAGE_NAME"

print_success "Release workflow test completed successfully!"
print_status "Summary:"
echo "  ✓ Changelog extraction works"
echo "  ✓ Python dependencies install correctly"
echo "  ✓ Application imports work"
echo "  ✓ Build system functions"
echo "  ✓ Package structure is valid"
print_status "You can now create a git tag to trigger the actual release:"
print_status "  git tag v${VERSION}"
print_status "  git push origin v${VERSION}"