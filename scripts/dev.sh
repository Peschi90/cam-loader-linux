#!/bin/bash
# Development script for CamLoader

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

print_status() {
    echo -e "${BLUE}[DEV]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# Setup development environment
setup_dev() {
    print_status "Setting up development environment..."
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
        python3 -m venv venv
    fi
    
    # Activate and install dependencies
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    
    # Install development dependencies
    pip install pytest black flake8
    
    print_success "Development environment ready"
}

# Run the application in development mode
run_dev() {
    print_status "Running CamLoader in development mode..."
    
    # Ensure virtual environment exists
    if [ ! -d "venv" ]; then
        setup_dev
    fi
    
    # Activate and run
    source venv/bin/activate
    cd src
    python main.py
}

# Run tests
run_tests() {
    print_status "Running tests..."
    
    source venv/bin/activate
    
    # Add src to Python path and run basic import tests
    PYTHONPATH=src python3 -c "
try:
    from camera.controller import CameraController
    from gui.main_window import CamLoaderMainWindow
    from config.manager import ConfigManager
    print('✓ All modules imported successfully')
except ImportError as e:
    print(f'✗ Import error: {e}')
    exit(1)
"
    
    print_success "Tests passed"
}

# Format code
format_code() {
    print_status "Formatting code with black..."
    
    source venv/bin/activate
    black src/ --line-length 88
    
    print_success "Code formatted"
}

# Lint code
lint_code() {
    print_status "Linting code with flake8..."
    
    source venv/bin/activate
    flake8 src/ --max-line-length=88 --ignore=E203,W503
    
    print_success "Linting completed"
}

# Clean build artifacts
clean() {
    print_status "Cleaning build artifacts..."
    
    rm -rf build/
    rm -rf dist/
    rm -rf *.egg-info/
    find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    
    print_success "Clean completed"
}

# Main function
case "${1:-help}" in
    setup)
        setup_dev
        ;;
    run)
        run_dev
        ;;
    test)
        run_tests
        ;;
    format)
        format_code
        ;;
    lint)
        lint_code
        ;;
    clean)
        clean
        ;;
    help|*)
        echo "CamLoader Development Script"
        echo ""
        echo "Usage: $0 <command>"
        echo ""
        echo "Commands:"
        echo "  setup   - Setup development environment"
        echo "  run     - Run application in development mode"
        echo "  test    - Run tests"
        echo "  format  - Format code with black"
        echo "  lint    - Lint code with flake8"
        echo "  clean   - Clean build artifacts"
        echo "  help    - Show this help message"
        ;;
esac