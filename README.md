# CamLoader - V4L2 Camera Parameter Controller# CamLoader - V4L2 Camera Parameter Controller



A user-friendly GUI application for controlling V4L2 camera parameters on Linux, developed as an alternative to guvcview with a focus on simplicity and maintainability.Eine benutzerfreundliche GUI-Anwendung zur Steuerung von V4L2-Kamera-Parametern unter Linux, entwickelt als Alternative zu guvcview mit Fokus auf Einfachheit und Wartbarkeit.



## 🎥 Screenshots## 🎥 Screenshots



![CamLoader Main Window](docs/screenshots/main-window.png)![CamLoader Main Window](docs/screenshots/main-window.png)

*Main window with parameter controls and live preview**Hauptfenster mit Parametersteuerung und Live-Vorschau*



## Features## Features



### 🎯 Main Functions### 🎯 Hauptfunktionen

- **Camera Detection**: Automatic detection of all available V4L2 cameras- **Kamera-Erkennung**: Automatische Erkennung aller verfügbaren V4L2-Kameras

- **Parameter Control**: Intuitive controls for all camera parameters (brightness, contrast, saturation, etc.)- **Parameter-Steuerung**: Intuitive Bedienelemente für alle Kamera-Parameter (Helligkeit, Kontrast, Sättigung, etc.)

- **Live Preview**: Real-time camera preview with configurable resolution- **Live-Vorschau**: Echtzeit-Kamera-Preview mit konfigurierbarer Auflösung

- **Configuration**: Save and load camera settings per camera- **Konfiguration**: Speichern und Laden von Kamera-Einstellungen pro Kamera

- **Backup System**: Automatic backup and restoration of original parameters- **Backup-System**: Automatische Sicherung und Wiederherstellung der Original-Parameter

- **Multi-Camera**: Support for multiple connected cameras simultaneously- **Multi-Kamera**: Unterstützung für mehrere angeschlossene Kameras gleichzeitig

- **Startup Configuration**: Automatic loading of settings at program startup- **Startup-Konfiguration**: Automatisches Laden von Einstellungen beim Programmstart

- **Parameter Tooltips**: Helpful descriptions for all parameters- **Parameter-Tooltips**: Hilfreiche Beschreibungen für alle Parameter

- **Lock Status**: Visualization of locked parameters- **Lock-Status**: Visualisierung von gesperrten Parametern

- **Detachable Preview**: Preview window can be detached- **Detachable Preview**: Vorschaufenster kann abgetrennt werden

- **CLI Support**: Command line arguments (--minimized, --debug, --version)- **CLI-Support**: Kommandozeilenargumente (--minimized, --debug, --version)



### 🛠 Technical Details### 🛠 Technische Details

- **Programming Language**: Python 3.8+ (GLIBC 2.17+ compatible)- **Programmiersprache**: Python 3.8+ (GLIBC 2.17+ kompatibel)

- **GUI Framework**: tkinter (system-wide available)- **GUI-Framework**: tkinter (systemweit verfügbar)

- **V4L2 Integration**: Direct v4l2-ctl commands for optimal compatibility- **V4L2-Integration**: Direkte v4l2-ctl Befehle für optimale Kompatibilität

- **Configuration**: JSON-based storage per camera- **Konfiguration**: JSON-basierte Speicherung pro Kamera

- **Architecture**: Modular structure for easy maintenance- **Architektur**: Modularer Aufbau für einfache Wartung

- **Build System**: GitHub Actions with PyInstaller- **Build-System**: GitHub Actions mit PyInstaller

- **Release**: Standalone Linux x86_64 Executable- **Release**: Standalone Linux x86_64 Executable



## 📥 Installation## 📥 Installation



### Precompiled Binary (recommended)### Vorkompiliertes Binary (empfohlen)



1. **Download latest version:**1. **Neueste Version herunterladen:**

   ```bash   ```bash

   # From GitHub Releases   # Von GitHub Releases

   wget https://github.com/Peschi90/cam-loader-linux/releases/latest/download/CamLoader-linux-x86_64   wget https://github.com/Peschi90/cam-loader-linux/releases/latest/download/CamLoader-linux-x86_64

   chmod +x CamLoader-linux-x86_64   chmod +x CamLoader-linux-x86_64

   ```   ```



2. **Start application:**2. **Anwendung starten:**

   ```bash   ```bash

   ./CamLoader-linux-x86_64   ./CamLoader-linux-x86_64

      

   # Or start minimized:   # Oder minimiert starten:

   ./CamLoader-linux-x86_64 --minimized   ./CamLoader-linux-x86_64 --minimized

      

   # With debug logging:   # Mit Debug-Logging:

   ./CamLoader-linux-x86_64 --debug   ./CamLoader-linux-x86_64 --debug

   ```   ```



### System Requirements### Systemanforderungen

- Linux distribution with V4L2 support (Ubuntu, Debian, Fedora, Arch, etc.)- Linux-Distribution mit V4L2-Unterstützung (Ubuntu, Debian, Fedora, Arch, etc.)

- x86_64 architecture- x86_64 Architektur

- GLIBC 2.17 or higher- GLIBC 2.17 oder höher

- v4l-utils installed- v4l-utils installiert

- Python 3.8+ (for running from source)- Python 3.8+ (für Ausführung aus Quellcode)



### Install v4l-utils### v4l-utils installieren



```bash```bash

# Ubuntu/Debian# Ubuntu/Debian

sudo apt install v4l-utilssudo apt install v4l-utils



# Fedora# Fedora

sudo dnf install v4l-utilssudo dnf install v4l-utils



# Arch Linux# Arch Linux

sudo pacman -S v4l-utilssudo pacman -S v4l-utils

``````



## 🚀 Usage## 🚀 Verwendung



### CLI Arguments### CLI-Argumente



```bash```bash

# Start normally# Normal starten

./CamLoader-linux-x86_64./CamLoader-linux-x86_64



# Start minimized (taskbar/tray)# Minimiert starten (Taskbar/Tray)

./CamLoader-linux-x86_64 --minimized./CamLoader-linux-x86_64 --minimized



# With debug logging# Mit Debug-Logging

./CamLoader-linux-x86_64 --debug./CamLoader-linux-x86_64 --debug



# Show version# Version anzeigen

./CamLoader-linux-x86_64 --version./CamLoader-linux-x86_64 --version

``````



### Getting Started### Erste Schritte



1. **Start application** - Available cameras will be detected automatically1. **Anwendung starten** - Verfügbare Kameras werden automatisch erkannt

2. **Select camera** from the dropdown list2. **Kamera auswählen** aus der Dropdown-Liste

3. **Adjust parameters** with sliders and input fields3. **Parameter anpassen** mit Schiebereglern und Eingabefeldern

4. **Start live preview** with the "Start Preview" button4. **Live-Vorschau starten** mit dem "Start Preview" Button

5. **Save settings** - Automatically saved per camera5. **Einstellungen speichern** - Werden automatisch pro Kamera gespeichert



### Menu Functions### Menü-Funktionen



#### File Menu#### File Menu

- **Save Configuration**: Save current parameters- **Save Configuration**: Aktuelle Parameter speichern

- **Load Configuration**: Load saved parameters- **Load Configuration**: Gespeicherte Parameter laden

- **Open Config Folder**: Open configuration directory- **Open Config Folder**: Konfigurationsverzeichnis öffnen

- **Exit**: Close application- **Exit**: Anwendung beenden



#### Camera Menu#### Camera Menu

- **Refresh Cameras**: Update camera list- **Refresh Cameras**: Kameraliste aktualisieren

- **Backup Parameters**: Backup original parameters- **Backup Parameters**: Original-Parameter sichern

- **Restore Parameters**: Restore parameters to original values- **Restore Parameters**: Parameter auf Original zurücksetzen

- **Startup Configuration**: Configure parameters for automatic startup- **Startup Configuration**: Parameter für automatischen Start konfigurieren



#### Help Menu#### Help Menu

- **GitHub Repository**: Open project page- **GitHub Repository**: Projekt-Seite öffnen

- **Report Issue**: Create bug/feature request on GitHub- **Report Issue**: Bug/Feature-Request auf GitHub erstellen

- **About**: About dialog with version information- **About**: Über-Dialog mit Versionsinformationen

- **Donate**: Support project via PayPal- **Donate**: Projekt mit PayPal unterstützen



### Configuration & Backups### Konfiguration & Backups



**Storage Location:****Speicherort:**

- Linux: `~/.camloader/` or `<project>/data/configs/`- Linux: `~/.camloader/` bzw. `<projekt>/data/configs/`

- Contains: Camera configurations and parameter backups- Enthält: Kamera-Konfigurationen und Parameter-Backups



**Access:****Zugriff:**

- Via Menu: `File → Open Config Folder`- Via Menu: `File → Open Config Folder`

- Via About Dialog: `📁 Open Config Folder` button- Via About-Dialog: `📁 Open Config Folder` Button



**Files:****Dateien:**

- `<device>_config.json`: Saved parameters- `<device>_config.json`: Gespeicherte Parameter

- `<device>_backup.json`: Original parameter backup- `<device>_backup.json`: Original-Parameter-Backup

- `startup_config.json`: Startup configuration- `startup_config.json`: Startup-Konfiguration



### Parameter Control### Parameter-Steuerung



The application automatically detects all available camera parameters:Die Anwendung erkennt automatisch alle verfügbaren Kamera-Parameter:



- **Brightness**: Base image brightness- **Helligkeit** (brightness): Grundhelligkeit des Bildes

- **Contrast**: Difference between light and dark areas- **Kontrast** (contrast): Unterschied zwischen hellen und dunklen Bereichen

- **Saturation**: Color intensity- **Sättigung** (saturation): Farbintensität

- **Hue**: Color shift- **Farbton** (hue): Farbverschiebung

- **White Balance**: Color temperature correction- **Weißabgleich** (white_balance_temperature): Farbtemperatur-Korrektur

- **Exposure**: Exposure control (exposure_auto, exposure_absolute)- **Belichtung** (exposure_auto, exposure_absolute): Belichtungssteuerung

- **Gain**: Signal amplification- **Verstärkung** (gain): Signalverstärkung

- **Sharpness**: Image sharpness- **Schärfe** (sharpness): Bildschärfe

- **And many more...**- **Und viele weitere...**



### Backup and Restore### Backup und Wiederherstellung



1. **Backup parameters:**1. **Parameter sichern:**

   - Select menu "Camera → Backup Parameters"   - Menü "Camera → Backup Parameters" wählen

   - Original values will be saved   - Ursprüngliche Werte werden gespeichert



2. **Restore parameters:**2. **Parameter wiederherstellen:**

   - Select menu "Camera → Restore Parameters"   - Menü "Camera → Restore Parameters" wählen

   - All parameters will be reset to original values   - Alle Parameter werden auf Originalwerte zurückgesetzt



### Configuration Management### Konfiguration verwalten



1. **Save:**1. **Speichern:**

   - Current state is automatically saved on exit   - Aktueller Zustand wird automatisch beim Beenden gespeichert

   - Manual save via "File → Save Configuration"   - Manuelles Speichern über "File → Save Configuration"



2. **Load:**2. **Laden:**

   - Saved settings are automatically loaded when switching cameras   - Gespeicherte Einstellungen werden beim Kamera-Wechsel automatisch geladen

   - Import/Export via "File → Load Configuration"   - Import/Export über "File → Load Configuration"



## Development## Entwicklung



### Setup Development Environment### Entwicklungsumgebung einrichten



```bash```bash

# Use development script# Development-Script verwenden

chmod +x scripts/dev.shchmod +x scripts/dev.sh

./scripts/dev.sh setup./scripts/dev.sh setup

``````



### Start Application in Development Mode### Anwendung in Development-Mode starten



```bash```bash

./scripts/dev.sh run./scripts/dev.sh run

``````



### Run Tests### Tests ausführen



```bash```bash

./scripts/dev.sh test./scripts/dev.sh test

``````



### Format Code### Code formatieren



```bash```bash

./scripts/dev.sh format./scripts/dev.sh format

``````



## 📁 Project Structure## 📁 Projektstruktur



``````

cam-loader-linux/cam-loader-linux/

├── src/                      # Main source code├── src/                      # Hauptquellcode

│   ├── main.py              # Entry point with CLI args│   ├── main.py              # Einstiegspunkt mit CLI-Args

│   ├── camera/              # Camera control│   ├── camera/              # Kamera-Steuerung

│   │   ├── __init__.py│   │   ├── __init__.py

│   │   ├── controller.py    # V4L2 integration│   │   ├── controller.py    # V4L2-Integration

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

