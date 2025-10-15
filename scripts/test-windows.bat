@echo off
REM Windows test script for CamLoader
REM This allows testing the GUI on Windows (without V4L2 functionality)

echo === CamLoader Windows Test ===

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or later
    pause
    exit /b 1
)

echo Python found

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install minimal dependencies for GUI testing
echo Installing minimal dependencies...
pip install --upgrade pip

REM Install only if user wants preview functionality
echo.
echo Do you want to install OpenCV for camera preview? (y/n)
set /p install_opencv=
if /i "%install_opencv%"=="y" (
    echo Installing OpenCV...
    pip install opencv-python
    pip install Pillow
) else (
    echo Skipping OpenCV installation - GUI will work without preview
)

echo.
echo Starting CamLoader in test mode...
echo Note: Camera functionality is simulated on Windows
echo.

REM Start the application
cd src
python main.py

echo.
echo CamLoader test session ended
pause