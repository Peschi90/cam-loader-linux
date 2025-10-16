# CamLoader - V4L2 Camera Parameter Controller# CamLoader - V4L2 Camera Parameter Controller# CamLoader - V4L2 Camera Parameter Controller



A user-friendly GUI application for controlling V4L2 camera parameters on Linux, developed as an alternative to guvcview with a focus on simplicity and maintainability.



## 🎥 ScreenshotsA user-friendly GUI application for controlling V4L2 camera parameters on Linux, developed as an alternative to guvcview with a focus on simplicity and maintainability.Eine benutzerfreundliche GUI-Anwendung zur Steuerung von V4L2-Kamera-Parametern unter Linux, entwickelt als Alternative zu guvcview mit Fokus auf Einfachheit und Wartbarkeit.



![CamLoader Main Window](docs/screenshots/main-window.png)

*Main window with parameter controls and live preview*

## 🎥 Screenshots## 🎥 Screenshots

## Features



### 🎯 Main Functions

- **Camera Detection**: Automatic detection of all available V4L2 cameras![CamLoader Main Window](docs/screenshots/main-window.png)![CamLoader Main Window](docs/screenshots/main-window.png)

- **Parameter Control**: Intuitive controls for all camera parameters (brightness, contrast, saturation, etc.)

- **Live Preview**: Real-time camera preview with configurable resolution*Main window with parameter controls and live preview**Hauptfenster mit Parametersteuerung und Live-Vorschau*

- **Configuration**: Save and load camera settings per camera

- **Backup System**: Automatic backup and restoration of original parameters

- **Multi-Camera**: Support for multiple connected cameras simultaneously

- **Startup Configuration**: Automatic loading of settings at program startup## Features## Features

- **Parameter Tooltips**: Helpful descriptions for all parameters

- **Lock Status**: Visualization of locked parameters

- **Detachable Preview**: Preview window can be detached

- **CLI Support**: Command line arguments (--minimized, --debug, --version)### 🎯 Main Functions### 🎯 Hauptfunktionen



### 🛠 Technical Details- **Camera Detection**: Automatic detection of all available V4L2 cameras- **Kamera-Erkennung**: Automatische Erkennung aller verfügbaren V4L2-Kameras

- **Programming Language**: Python 3.8+ (GLIBC 2.17+ compatible)

- **GUI Framework**: tkinter (system-wide available)- **Parameter Control**: Intuitive controls for all camera parameters (brightness, contrast, saturation, etc.)- **Parameter-Steuerung**: Intuitive Bedienelemente für alle Kamera-Parameter (Helligkeit, Kontrast, Sättigung, etc.)

- **V4L2 Integration**: Direct v4l2-ctl commands for optimal compatibility

- **Configuration**: JSON-based storage per camera- **Live Preview**: Real-time camera preview with configurable resolution- **Live-Vorschau**: Echtzeit-Kamera-Preview mit konfigurierbarer Auflösung

- **Architecture**: Modular structure for easy maintenance

- **Build System**: GitHub Actions with PyInstaller- **Configuration**: Save and load camera settings per camera- **Konfiguration**: Speichern und Laden von Kamera-Einstellungen pro Kamera

- **Release**: Standalone Linux x86_64 Executable

- **Backup System**: Automatic backup and restoration of original parameters- **Backup-System**: Automatische Sicherung und Wiederherstellung der Original-Parameter

## 📥 Installation

- **Multi-Camera**: Support for multiple connected cameras simultaneously- **Multi-Kamera**: Unterstützung für mehrere angeschlossene Kameras gleichzeitig

### Precompiled Binary (recommended)

- **Startup Configuration**: Automatic loading of settings at program startup- **Startup-Konfiguration**: Automatisches Laden von Einstellungen beim Programmstart

1. **Download latest version:**

   ```bash- **Parameter Tooltips**: Helpful descriptions for all parameters- **Parameter-Tooltips**: Hilfreiche Beschreibungen für alle Parameter

   # From GitHub Releases

   wget https://github.com/Peschi90/cam-loader-linux/releases/latest/download/CamLoader-linux-x86_64- **Lock Status**: Visualization of locked parameters- **Lock-Status**: Visualisierung von gesperrten Parametern

   chmod +x CamLoader-linux-x86_64

   ```- **Detachable Preview**: Preview window can be detached- **Detachable Preview**: Vorschaufenster kann abgetrennt werden



2. **Start application:**- **CLI Support**: Command line arguments (--minimized, --debug, --version)- **CLI-Support**: Kommandozeilenargumente (--minimized, --debug, --version)

   ```bash

   ./CamLoader-linux-x86_64

   

   # Or start minimized:### 🛠 Technical Details### 🛠 Technische Details

   ./CamLoader-linux-x86_64 --minimized

   - **Programming Language**: Python 3.8+ (GLIBC 2.17+ compatible)- **Programmiersprache**: Python 3.8+ (GLIBC 2.17+ kompatibel)

   # With debug logging:

   ./CamLoader-linux-x86_64 --debug- **GUI Framework**: tkinter (system-wide available)- **GUI-Framework**: tkinter (systemweit verfügbar)

   ```

- **V4L2 Integration**: Direct v4l2-ctl commands for optimal compatibility- **V4L2-Integration**: Direkte v4l2-ctl Befehle für optimale Kompatibilität

### System Requirements

- Linux distribution with V4L2 support (Ubuntu, Debian, Fedora, Arch, etc.)- **Configuration**: JSON-based storage per camera- **Konfiguration**: JSON-basierte Speicherung pro Kamera

- x86_64 architecture

- GLIBC 2.17 or higher- **Architecture**: Modular structure for easy maintenance- **Architektur**: Modularer Aufbau für einfache Wartung

- v4l-utils installed

- Python 3.8+ (for running from source)- **Build System**: GitHub Actions with PyInstaller- **Build-System**: GitHub Actions mit PyInstaller



### Install v4l-utils- **Release**: Standalone Linux x86_64 Executable- **Release**: Standalone Linux x86_64 Executable



```bash

# Ubuntu/Debian

sudo apt install v4l-utils## 📥 Installation## 📥 Installation



# Fedora

sudo dnf install v4l-utils

### Precompiled Binary (recommended)### Vorkompiliertes Binary (empfohlen)

# Arch Linux

sudo pacman -S v4l-utils

```

1. **Download latest version:**1. **Neueste Version herunterladen:**

## 🚀 Usage

   ```bash   ```bash

### CLI Arguments

   # From GitHub Releases   # Von GitHub Releases

```bash

# Start normally   wget https://github.com/Peschi90/cam-loader-linux/releases/latest/download/CamLoader-linux-x86_64   wget https://github.com/Peschi90/cam-loader-linux/releases/latest/download/CamLoader-linux-x86_64

./CamLoader-linux-x86_64

   chmod +x CamLoader-linux-x86_64   chmod +x CamLoader-linux-x86_64

# Start minimized (taskbar/tray)

./CamLoader-linux-x86_64 --minimized   ```   ```



# With debug logging

./CamLoader-linux-x86_64 --debug

2. **Start application:**2. **Anwendung starten:**

# Show version

./CamLoader-linux-x86_64 --version   ```bash   ```bash

```

   ./CamLoader-linux-x86_64   ./CamLoader-linux-x86_64

### Getting Started

      

1. **Start application** - Available cameras will be detected automatically

2. **Select camera** from the dropdown list   # Or start minimized:   # Oder minimiert starten:

3. **Adjust parameters** with sliders and input fields

4. **Start live preview** with the "Start Preview" button   ./CamLoader-linux-x86_64 --minimized   ./CamLoader-linux-x86_64 --minimized

5. **Save settings** - Automatically saved per camera

      

### Menu Functions

   # With debug logging:   # Mit Debug-Logging:

#### File Menu

- **Save Configuration**: Save current parameters   ./CamLoader-linux-x86_64 --debug   ./CamLoader-linux-x86_64 --debug

- **Load Configuration**: Load saved parameters

- **Open Config Folder**: Open configuration directory   ```   ```

- **Exit**: Close application



#### Camera Menu

- **Refresh Cameras**: Update camera list### System Requirements### Systemanforderungen

- **Backup Parameters**: Backup original parameters

- **Restore Parameters**: Restore parameters to original values- Linux distribution with V4L2 support (Ubuntu, Debian, Fedora, Arch, etc.)- Linux-Distribution mit V4L2-Unterstützung (Ubuntu, Debian, Fedora, Arch, etc.)

- **Startup Configuration**: Configure parameters for automatic startup

- x86_64 architecture- x86_64 Architektur

#### Help Menu

- **GitHub Repository**: Open project page- GLIBC 2.17 or higher- GLIBC 2.17 oder höher

- **Report Issue**: Create bug/feature request on GitHub

- **About**: About dialog with version information- v4l-utils installed- v4l-utils installiert

- **Donate**: Support project via PayPal

- Python 3.8+ (for running from source)- Python 3.8+ (für Ausführung aus Quellcode)

### Configuration & Backups



**Storage Location:**

- Linux: `~/.camloader/` or `<project>/data/configs/`### Install v4l-utils### v4l-utils installieren

- Contains: Camera configurations and parameter backups



**Access:**

- Via Menu: `File → Open Config Folder````bash```bash

- Via About Dialog: `📁 Open Config Folder` button

# Ubuntu/Debian# Ubuntu/Debian

**Files:**

- `<device>_config.json`: Saved parameterssudo apt install v4l-utilssudo apt install v4l-utils

- `<device>_backup.json`: Original parameter backup

- `startup_config.json`: Startup configuration



### Parameter Control# Fedora# Fedora



The application automatically detects all available camera parameters:sudo dnf install v4l-utilssudo dnf install v4l-utils



- **Brightness**: Base image brightness

- **Contrast**: Difference between light and dark areas

- **Saturation**: Color intensity# Arch Linux# Arch Linux

- **Hue**: Color shift

- **White Balance**: Color temperature correctionsudo pacman -S v4l-utilssudo pacman -S v4l-utils

- **Exposure**: Exposure control (exposure_auto, exposure_absolute)

- **Gain**: Signal amplification``````

- **Sharpness**: Image sharpness

- **And many more...**



### Backup and Restore## 🚀 Usage## 🚀 Verwendung



1. **Backup parameters:**

   - Select menu "Camera → Backup Parameters"

   - Original values will be saved### CLI Arguments### CLI-Argumente



2. **Restore parameters:**

   - Select menu "Camera → Restore Parameters"

   - All parameters will be reset to original values```bash```bash



### Configuration Management# Start normally# Normal starten



1. **Save:**./CamLoader-linux-x86_64./CamLoader-linux-x86_64

   - Current state is automatically saved on exit

   - Manual save via "File → Save Configuration"



2. **Load:**# Start minimized (taskbar/tray)# Minimiert starten (Taskbar/Tray)

   - Saved settings are automatically loaded when switching cameras

   - Import/Export via "File → Load Configuration"./CamLoader-linux-x86_64 --minimized./CamLoader-linux-x86_64 --minimized



## Development



### Setup Development Environment# With debug logging# Mit Debug-Logging



```bash./CamLoader-linux-x86_64 --debug./CamLoader-linux-x86_64 --debug

# Use development script

chmod +x scripts/dev.sh

./scripts/dev.sh setup

```# Show version# Version anzeigen



### Start Application in Development Mode./CamLoader-linux-x86_64 --version./CamLoader-linux-x86_64 --version



```bash``````

./scripts/dev.sh run

```



### Run Tests### Getting Started### Erste Schritte



```bash

./scripts/dev.sh test

```1. **Start application** - Available cameras will be detected automatically1. **Anwendung starten** - Verfügbare Kameras werden automatisch erkannt



### Format Code2. **Select camera** from the dropdown list2. **Kamera auswählen** aus der Dropdown-Liste



```bash3. **Adjust parameters** with sliders and input fields3. **Parameter anpassen** mit Schiebereglern und Eingabefeldern

./scripts/dev.sh format

```4. **Start live preview** with the "Start Preview" button4. **Live-Vorschau starten** mit dem "Start Preview" Button



## 📁 Project Structure5. **Save settings** - Automatically saved per camera5. **Einstellungen speichern** - Werden automatisch pro Kamera gespeichert



```

cam-loader-linux/

├── src/                      # Main source code### Menu Functions### Menü-Funktionen

│   ├── main.py              # Entry point with CLI args

│   ├── camera/              # Camera control

│   │   ├── __init__.py

│   │   ├── controller.py    # V4L2 integration#### File Menu#### File Menu

│   │   └── device.py        # Camera device model

│   ├── gui/                 # User interface- **Save Configuration**: Save current parameters- **Save Configuration**: Aktuelle Parameter speichern

│   │   ├── __init__.py

│   │   ├── main_window.py   # Main window- **Load Configuration**: Load saved parameters- **Load Configuration**: Gespeicherte Parameter laden

│   │   ├── parameter_frame.py  # Parameter controls

│   │   ├── preview_frame.py    # Live preview- **Open Config Folder**: Open configuration directory- **Open Config Folder**: Konfigurationsverzeichnis öffnen

│   │   ├── detached_preview.py # Detachable preview window

│   │   └── startup_config.py   # Startup config dialog- **Exit**: Close application- **Exit**: Anwendung beenden

│   ├── config/              # Configuration

│   │   ├── __init__.py

│   │   └── manager.py       # Config management

│   └── utils/               # Utilities#### Camera Menu#### Camera Menu

│       ├── __init__.py

│       └── logger.py        # Logging setup- **Refresh Cameras**: Update camera list- **Refresh Cameras**: Kameraliste aktualisieren

├── data/                    # Configuration files

│   └── configs/            # Saved camera configs & backups- **Backup Parameters**: Backup original parameters- **Backup Parameters**: Original-Parameter sichern

├── .github/                # GitHub Actions

│   └── workflows/- **Restore Parameters**: Restore parameters to original values- **Restore Parameters**: Parameter auf Original zurücksetzen

│       └── build.yml       # Automated build pipeline

├── requirements.txt        # Python dependencies- **Startup Configuration**: Configure parameters for automatic startup- **Startup Configuration**: Parameter für automatischen Start konfigurieren

├── CHANGELOG.md           # Version history

└── README.md              # This file

```

#### Help Menu#### Help Menu

## Architecture

- **GitHub Repository**: Open project page- **GitHub Repository**: Projekt-Seite öffnen

### Modular Structure

- **Report Issue**: Create bug/feature request on GitHub- **Report Issue**: Bug/Feature-Request auf GitHub erstellen

1. **Camera Module** (`src/camera/`):

   - V4L2 device detection- **About**: About dialog with version information- **About**: Über-Dialog mit Versionsinformationen

   - Parameter management

   - Backup/Restore functionality- **Donate**: Support project via PayPal- **Donate**: Projekt mit PayPal unterstützen



2. **GUI Module** (`src/gui/`):

   - Main window with menus

   - Parameter control with various widget types### Configuration & Backups### Konfiguration & Backups

   - Live camera preview



3. **Config Module** (`src/config/`):

   - JSON-based configuration management**Storage Location:****Speicherort:**

   - Per-camera settings

   - Import/Export functions- Linux: `~/.camloader/` or `<project>/data/configs/`- Linux: `~/.camloader/` bzw. `<projekt>/data/configs/`



4. **Utils Module** (`src/utils/`):- Contains: Camera configurations and parameter backups- Enthält: Kamera-Konfigurationen und Parameter-Backups

   - Logging configuration

   - Common utility functions



### Data Flow**Access:****Zugriff:**



```- Via Menu: `File → Open Config Folder`- Via Menu: `File → Open Config Folder`

V4L2 Cameras → CameraController → GUI → ConfigManager

                     ↑                        ↓- Via About Dialog: `📁 Open Config Folder` button- Via About-Dialog: `📁 Open Config Folder` Button

               Parameter Updates          JSON Files

```



## 🐛 Troubleshooting**Files:****Dateien:**



### Common Issues- `<device>_config.json`: Saved parameters- `<device>_config.json`: Gespeicherte Parameter



1. **No cameras found:**- `<device>_backup.json`: Original parameter backup- `<device>_backup.json`: Original-Parameter-Backup

   ```bash

   # Check available cameras- `startup_config.json`: Startup configuration- `startup_config.json`: Startup-Konfiguration

   ls /dev/video*

   v4l2-ctl --list-devices

   ```

### Parameter Control### Parameter-Steuerung

2. **Permission errors:**

   ```bash

   # Add user to video group

   sudo usermod -a -G video $USERThe application automatically detects all available camera parameters:Die Anwendung erkennt automatisch alle verfügbaren Kamera-Parameter:

   # Re-login required!

   ```



3. **--minimized doesn't work:**- **Brightness**: Base image brightness- **Helligkeit** (brightness): Grundhelligkeit des Bildes

   - On Linux: Window manager must support iconify()

   - Test: `./CamLoader-linux-x86_64 --minimized --debug`- **Contrast**: Difference between light and dark areas- **Kontrast** (contrast): Unterschied zwischen hellen und dunklen Bereichen

   - Log message: "Started in minimized state" should appear

- **Saturation**: Color intensity- **Sättigung** (saturation): Farbintensität

4. **OpenCV/Preview problems:**

   ```bash- **Hue**: Color shift- **Farbton** (hue): Farbverschiebung

   # Check system info

   v4l2-ctl --device=/dev/video0 --list-formats-ext- **White Balance**: Color temperature correction- **Weißabgleich** (white_balance_temperature): Farbtemperatur-Korrektur

   ```

- **Exposure**: Exposure control (exposure_auto, exposure_absolute)- **Belichtung** (exposure_auto, exposure_absolute): Belichtungssteuerung

5. **Config folder not found:**

   - Check in About dialog: `Help → About → Config/Backup Location`- **Gain**: Signal amplification- **Verstärkung** (gain): Signalverstärkung

   - Or via Menu: `File → Open Config Folder`

- **Sharpness**: Image sharpness- **Schärfe** (sharpness): Bildschärfe

### Debug Mode

- **And many more...**- **Und viele weitere...**

Detailed logs with debug mode:

```bash

./CamLoader-linux-x86_64 --debug

```### Backup and Restore### Backup und Wiederherstellung



**Important log messages:**

- `"Startup complete - parameter changes will now be applied"` - Initialization complete

- `"Started in minimized state"` - Minimization successful1. **Backup parameters:**1. **Parameter sichern:**

- `"Applied startup config for..."` - Startup config loaded

- `"Loaded saved config for..."` - Saved config loaded   - Select menu "Camera → Backup Parameters"   - Menü "Camera → Backup Parameters" wählen



### Support & Issues   - Original values will be saved   - Ursprüngliche Werte werden gespeichert



🐛 **Report bugs:**

- Via Menu: `Help → Report Issue`

- Or directly: [GitHub Issues](https://github.com/Peschi90/cam-loader-linux/issues/new)2. **Restore parameters:**2. **Parameter wiederherstellen:**



📖 **Documentation:**   - Select menu "Camera → Restore Parameters"   - Menü "Camera → Restore Parameters" wählen

- GitHub Repository: [Peschi90/cam-loader-linux](https://github.com/Peschi90/cam-loader-linux)

- CHANGELOG: See [CHANGELOG.md](CHANGELOG.md)   - All parameters will be reset to original values   - Alle Parameter werden auf Originalwerte zurückgesetzt



## 🚧 Known Limitations



- **Linux only**: Exclusively for Linux systems with V4L2 support### Configuration Management### Konfiguration verwalten

- **Camera support**: Depends on V4L2 driver quality

- **Simultaneous usage**: Camera cannot be used by multiple applications simultaneously

- **Window Manager**: Minimized start requires X11/Wayland window manager support

1. **Save:**1. **Speichern:**

## 🗺 Roadmap

   - Current state is automatically saved on exit   - Aktueller Zustand wird automatisch beim Beenden gespeichert

### Version 1.0 (Planned)

- [x] ~~Standalone binary with GitHub Actions~~   - Manual save via "File → Save Configuration"   - Manuelles Speichern über "File → Save Configuration"

- [x] ~~CLI arguments (--minimized, --debug, --version)~~

- [x] ~~Startup configuration~~

- [x] ~~Parameter lock visualization~~

- [x] ~~Detachable preview window~~2. **Load:**2. **Laden:**

- [x] ~~GitHub issue integration~~

- [x] ~~Config folder access~~   - Saved settings are automatically loaded when switching cameras   - Gespeicherte Einstellungen werden beim Kamera-Wechsel automatisch geladen



### Future Features   - Import/Export via "File → Load Configuration"   - Import/Export über "File → Load Configuration"

- [ ] Plugin system for extended parameters

- [ ] Scripting support for automation

- [ ] Extended preview options (histogram, waveform, etc.)

- [ ] Multi-language support (EN, DE, etc.)## Development## Entwicklung

- [ ] Dark theme / theme system

- [ ] Camera profile management

- [ ] Batch parameter export/import

### Setup Development Environment### Entwicklungsumgebung einrichten

## 🤝 Contributing



Contributions are welcome!

```bash```bash

### How to contribute:

# Use development script# Development-Script verwenden

1. Fork the repository

2. Create feature branch (`git checkout -b feature/new-feature`)chmod +x scripts/dev.shchmod +x scripts/dev.sh

3. Commit changes (`git commit -m 'Add new feature'`)

4. Push branch (`git push origin feature/new-feature`)./scripts/dev.sh setup./scripts/dev.sh setup

5. Create pull request

``````

### Development



```bash

# Clone repository### Start Application in Development Mode### Anwendung in Development-Mode starten

git clone https://github.com/Peschi90/cam-loader-linux.git

cd cam-loader-linux



# Install dependencies```bash```bash

pip install -r requirements.txt

./scripts/dev.sh run./scripts/dev.sh run

# Run application

python src/main.py --debug``````

```



### Coding Standards

### Run Tests### Tests ausführen

- Follow Python PEP 8 Style Guide

- Docstrings for all functions and classes

- Modular, testable code

- Meaningful commit messages (Conventional Commits)```bash```bash

- Comments in English for international contributors

./scripts/dev.sh test./scripts/dev.sh test

## 💝 Support

``````

### Find CamLoader helpful?



☕ **Donate via PayPal:** [paypal.me/i3ull3t](https://paypal.me/i3ull3t)

### Format Code### Code formatieren

Or:

- ⭐ Give the project a star on GitHub

- 🐛 Report bugs and suggest features

- 📖 Improve documentation```bash```bash

- 🔧 Contribute code

./scripts/dev.sh format./scripts/dev.sh format

## 📄 License

``````

MIT License - see [LICENSE](LICENSE) file for details.



## 🙏 Acknowledgments

## 📁 Project Structure## 📁 Projektstruktur

- **V4L2 Team**: For the excellent Video4Linux2 API

- **Python Community**: For tkinter and all dependencies

- **OpenCV Project**: For video functionality

- **All Contributors**: Thank you for your support!``````



## 📬 Contactcam-loader-linux/cam-loader-linux/



- **Developer**: I3uLL3t├── src/                      # Main source code├── src/                      # Hauptquellcode

- **GitHub**: [@Peschi90](https://github.com/Peschi90)

- **Repository**: [cam-loader-linux](https://github.com/Peschi90/cam-loader-linux)│   ├── main.py              # Entry point with CLI args│   ├── main.py              # Einstiegspunkt mit CLI-Args

- **Issues**: [Report Bug/Feature](https://github.com/Peschi90/cam-loader-linux/issues/new)

- **Donate**: [PayPal](https://paypal.me/i3ull3t)│   ├── camera/              # Camera control│   ├── camera/              # Kamera-Steuerung



---│   │   ├── __init__.py│   │   ├── __init__.py



**CamLoader** - Simple and powerful V4L2 camera control for Linux 🎥✨│   │   ├── controller.py    # V4L2 integration│   │   ├── controller.py    # V4L2-Integration


│   │   └── device.py        # Camera device model│   │   └── device.py        # Camera-Device-Model

│   ├── gui/                 # User interface│   ├── gui/                 # Benutzeroberfläche

│   │   ├── __init__.py│   │   ├── __init__.py

│   │   ├── main_window.py   # Main window│   │   ├── main_window.py   # Hauptfenster

│   │   ├── parameter_frame.py  # Parameter controls│   │   ├── parameter_frame.py  # Parameter-Controls

│   │   ├── preview_frame.py    # Live preview│   │   ├── preview_frame.py    # Live-Vorschau

│   │   ├── detached_preview.py # Detachable preview window│   │   ├── detached_preview.py # Abtrennbares Vorschaufenster

│   │   └── startup_config.py   # Startup config dialog│   │   └── startup_config.py   # Startup-Config-Dialog

│   ├── config/              # Configuration│   ├── config/              # Konfiguration

│   │   ├── __init__.py│   │   ├── __init__.py

│   │   └── manager.py       # Config management│   │   └── manager.py       # Config-Management

│   └── utils/               # Utilities│   └── utils/               # Hilfsfunktionen

│       ├── __init__.py│       ├── __init__.py

│       └── logger.py        # Logging setup│       └── logger.py        # Logging-Setup

├── data/                    # Configuration files├── data/                    # Konfigurationsdateien

│   └── configs/            # Saved camera configs & backups│   └── configs/            # Gespeicherte Kamera-Configs & Backups

├── .github/                # GitHub Actions├── .github/                # GitHub Actions

│   └── workflows/│   └── workflows/

│       └── build.yml       # Automated build pipeline│       └── build.yml       # Automated Build Pipeline

├── requirements.txt        # Python dependencies├── requirements.txt        # Python-Abhängigkeiten

├── CHANGELOG.md           # Version history├── CHANGELOG.md           # Versions-Historie

└── README.md              # This file└── README.md              # Diese Datei

``````



## Architecture## Architektur



### Modular Structure### Modularer Aufbau



1. **Camera Module** (`src/camera/`):1. **Camera Module** (`src/camera/`):

   - V4L2 device detection   - V4L2-Geräteerkennung

   - Parameter management   - Parameter-Management

   - Backup/Restore functionality   - Backup/Restore-Funktionalität



2. **GUI Module** (`src/gui/`):2. **GUI Module** (`src/gui/`):

   - Main window with menus   - Hauptfenster mit Menüs

   - Parameter control with various widget types   - Parameter-Steuerung mit verschiedenen Widget-Typen

   - Live camera preview   - Live-Kamera-Vorschau



3. **Config Module** (`src/config/`):3. **Config Module** (`src/config/`):

   - JSON-based configuration management   - JSON-basierte Konfigurationsverwaltung

   - Per-camera settings   - Pro-Kamera Einstellungen

   - Import/Export functions   - Import/Export-Funktionen



4. **Utils Module** (`src/utils/`):4. **Utils Module** (`src/utils/`):

   - Logging configuration   - Logging-Konfiguration

   - Common utility functions   - Gemeinsame Hilfsfunktionen



### Data Flow### Datenfluss



``````

V4L2 Cameras → CameraController → GUI → ConfigManagerV4L2-Kameras → CameraController → GUI → ConfigManager

                     ↑                        ↓                     ↑                        ↓

               Parameter Updates          JSON Files               Parameter-Updates          JSON-Dateien

``````



## 🐛 Troubleshooting## 🐛 Fehlerbehebung



### Common Issues### Häufige Probleme



1. **No cameras found:**1. **Keine Kameras gefunden:**

   ```bash   ```bash

   # Check available cameras   # Verfügbare Kameras prüfen

   ls /dev/video*   ls /dev/video*

   v4l2-ctl --list-devices   v4l2-ctl --list-devices

   ```   ```



2. **Permission errors:**2. **Permission-Fehler:**

   ```bash   ```bash

   # Add user to video group   # Benutzer zur video-Gruppe hinzufügen

   sudo usermod -a -G video $USER   sudo usermod -a -G video $USER

   # Re-login required!   # Neuanmeldung erforderlich!

   ```   ```



3. **--minimized doesn't work:**3. **--minimized funktioniert nicht:**

   - On Linux: Window manager must support iconify()   - Unter Linux: Window Manager muss iconify() unterstützen

   - Test: `./CamLoader-linux-x86_64 --minimized --debug`   - Testen: `./CamLoader-linux-x86_64 --minimized --debug`

   - Log message: "Started in minimized state" should appear   - Log-Nachricht: "Started in minimized state" sollte erscheinen



4. **OpenCV/Preview problems:**4. **OpenCV/Preview-Probleme:**

   ```bash   ```bash

   # Check system info   # System-Info prüfen

   v4l2-ctl --device=/dev/video0 --list-formats-ext   v4l2-ctl --device=/dev/video0 --list-formats-ext

   ```   ```



5. **Config folder not found:**5. **Config-Folder nicht gefunden:**

   - Check in About dialog: `Help → About → Config/Backup Location`   - Im About-Dialog nachsehen: `Help → About → Config/Backup Location`

   - Or via Menu: `File → Open Config Folder`   - Oder via Menu: `File → Open Config Folder`



### Debug Mode### Debug-Modus



Detailed logs with debug mode:Detaillierte Logs mit Debug-Modus:

```bash```bash

./CamLoader-linux-x86_64 --debug./CamLoader-linux-x86_64 --debug

``````



**Important log messages:****Wichtige Log-Nachrichten:**

- `"Startup complete - parameter changes will now be applied"` - Initialization complete- `"Startup complete - parameter changes will now be applied"` - Init fertig

- `"Started in minimized state"` - Minimization successful- `"Started in minimized state"` - Minimierung erfolgreich

- `"Applied startup config for..."` - Startup config loaded- `"Applied startup config for..."` - Startup-Config geladen

- `"Loaded saved config for..."` - Saved config loaded- `"Loaded saved config for..."` - Gespeicherte Config geladen



### Support & Issues### Support & Issues



🐛 **Report bugs:**🐛 **Bug melden:**

- Via Menu: `Help → Report Issue`- Via Menu: `Help → Report Issue`

- Or directly: [GitHub Issues](https://github.com/Peschi90/cam-loader-linux/issues/new)- Oder direkt: [GitHub Issues](https://github.com/Peschi90/cam-loader-linux/issues/new)



📖 **Documentation:**📖 **Dokumentation:**

- GitHub Repository: [Peschi90/cam-loader-linux](https://github.com/Peschi90/cam-loader-linux)- GitHub Repository: [Peschi90/cam-loader-linux](https://github.com/Peschi90/cam-loader-linux)

- CHANGELOG: See [CHANGELOG.md](CHANGELOG.md)- CHANGELOG: Siehe [CHANGELOG.md](CHANGELOG.md)



## 🚧 Known Limitations## 🚧 Bekannte Einschränkungen



- **Linux only**: Exclusively for Linux systems with V4L2 support- **Nur Linux**: Ausschließlich für Linux-Systeme mit V4L2-Unterstützung

- **Camera support**: Depends on V4L2 driver quality- **Kamera-Unterstützung**: Abhängig von V4L2-Treiber-Qualität

- **Simultaneous usage**: Camera cannot be used by multiple applications simultaneously- **Simultane Nutzung**: Kamera kann nicht gleichzeitig von mehreren Anwendungen verwendet werden

- **Window Manager**: Minimized start requires X11/Wayland window manager support- **Window Manager**: Minimized-Start erfordert X11/Wayland Window Manager Unterstützung



## 🗺 Roadmap## 🗺 Roadmap



### Version 1.0 (Planned)### Version 1.0 (Planned)

- [x] ~~Standalone binary with GitHub Actions~~- [x] ~~Standalone-Binary mit GitHub Actions~~

- [x] ~~CLI arguments (--minimized, --debug, --version)~~- [x] ~~CLI-Argumente (--minimized, --debug, --version)~~

- [x] ~~Startup configuration~~- [x] ~~Startup-Konfiguration~~

- [x] ~~Parameter lock visualization~~- [x] ~~Parameter-Lock-Visualisierung~~

- [x] ~~Detachable preview window~~- [x] ~~Detachable Preview Window~~

- [x] ~~GitHub issue integration~~- [x] ~~GitHub Issue Integration~~

- [x] ~~Config folder access~~- [x] ~~Config-Folder-Zugriff~~



### Future Features### Future Features

- [ ] Plugin system for extended parameters- [ ] Plugin-System für erweiterte Parameter

- [ ] Scripting support for automation- [ ] Scripting-Unterstützung für Automatisierung

- [ ] Extended preview options (histogram, waveform, etc.)- [ ] Erweiterte Vorschau-Optionen (Histogramm, Waveform, etc.)

- [ ] Multi-language support (EN, DE, etc.)- [ ] Multi-Language-Unterstützung (EN, DE, etc.)

- [ ] Dark theme / theme system- [ ] Dark Theme / Theme-System

- [ ] Camera profile management- [ ] Kamera-Profile-Management

- [ ] Batch parameter export/import- [ ] Batch-Parameter-Export/Import



## 🤝 Contributing## 🤝 Beitragen



Contributions are welcome!Beiträge sind willkommen! 



### How to contribute:### Wie man beiträgt:



1. Fork the repository1. Fork des Repositories erstellen

2. Create feature branch (`git checkout -b feature/new-feature`)2. Feature-Branch erstellen (`git checkout -b feature/neue-funktion`)

3. Commit changes (`git commit -m 'Add new feature'`)3. Änderungen committen (`git commit -m 'Neue Funktion hinzugefügt'`)

4. Push branch (`git push origin feature/new-feature`)4. Branch pushen (`git push origin feature/neue-funktion`)

5. Create pull request5. Pull Request erstellen



### Development### Entwicklung



```bash```bash

# Clone repository# Repository klonen

git clone https://github.com/Peschi90/cam-loader-linux.gitgit clone https://github.com/Peschi90/cam-loader-linux.git

cd cam-loader-linuxcd cam-loader-linux



# Install dependencies# Abhängigkeiten installieren

pip install -r requirements.txtpip install -r requirements.txt



# Run application# Anwendung ausführen

python src/main.py --debugpython src/main.py --debug

``````



### Coding Standards### Coding Standards



- Follow Python PEP 8 Style Guide- Python PEP 8 Style Guide befolgen

- Docstrings for all functions and classes- Docstrings für alle Funktionen und Klassen

- Modular, testable code- Modularer, testbarer Code

- Meaningful commit messages (Conventional Commits)- Aussagekräftige Commit-Messages (Conventional Commits)

- Comments in English for international contributors- Deutsche Kommentare für User-facing Features



## 💝 Support## 💝 Support



### Find CamLoader helpful?### Du findest CamLoader hilfreich?



☕ **Donate via PayPal:** [paypal.me/i3ull3t](https://paypal.me/i3ull3t)☕ **Spende via PayPal:** [paypal.me/i3ull3t](https://paypal.me/i3ull3t)



Or:Oder:

- ⭐ Give the project a star on GitHub- ⭐ Gib dem Projekt einen Star auf GitHub

- 🐛 Report bugs and suggest features- 🐛 Melde Bugs und schlage Features vor

- 📖 Improve documentation- 📖 Verbessere die Dokumentation

- 🔧 Contribute code- 🔧 Contribue Code



## 📄 License## 📄 Lizenz



MIT License - see [LICENSE](LICENSE) file for details.MIT License - siehe [LICENSE](LICENSE) Datei für Details.



## 🙏 Acknowledgments## 🙏 Danksagungen



- **V4L2 Team**: For the excellent Video4Linux2 API- **V4L2-Team**: Für die hervorragende Video4Linux2 API

- **Python Community**: For tkinter and all dependencies- **Python Community**: Für tkinter und alle Dependencies

- **OpenCV Project**: For video functionality- **OpenCV Project**: Für Video-Funktionalität

- **All Contributors**: Thank you for your support!- **Alle Contributors**: Danke für eure Unterstützung!



## 📬 Contact## 📬 Kontakt



- **Developer**: I3uLL3t- **Developer**: I3uLL3t

- **GitHub**: [@Peschi90](https://github.com/Peschi90)- **GitHub**: [@Peschi90](https://github.com/Peschi90)

- **Repository**: [cam-loader-linux](https://github.com/Peschi90/cam-loader-linux)- **Repository**: [cam-loader-linux](https://github.com/Peschi90/cam-loader-linux)

- **Issues**: [Report Bug/Feature](https://github.com/Peschi90/cam-loader-linux/issues/new)- **Issues**: [Report Bug/Feature](https://github.com/Peschi90/cam-loader-linux/issues/new)

- **Donate**: [PayPal](https://paypal.me/i3ull3t)- **Donate**: [PayPal](https://paypal.me/i3ull3t)



------



**CamLoader** - Simple and powerful V4L2 camera control for Linux 🎥✨**CamLoader** - Einfache und leistungsstarke V4L2-Kamerasteuerung für Linux 🎥✨

