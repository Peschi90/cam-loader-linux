# CamLoader - V4L2 Camera Parameter Controller

Eine benutzerfreundliche GUI-Anwendung zur Steuerung von V4L2-Kamera-Parametern unter Linux, entwickelt als Alternative zu guvcview mit Fokus auf Einfachheit und Wartbarkeit.

## 🎥 Screenshots

![CamLoader Main Window](docs/screenshots/main-window.png)
*Hauptfenster mit Parametersteuerung und Live-Vorschau*

## Features

### 🎯 Hauptfunktionen
- **Kamera-Erkennung**: Automatische Erkennung aller verfügbaren V4L2-Kameras
- **Parameter-Steuerung**: Intuitive Bedienelemente für alle Kamera-Parameter (Helligkeit, Kontrast, Sättigung, etc.)
- **Live-Vorschau**: Echtzeit-Kamera-Preview mit konfigurierbarer Auflösung
- **Konfiguration**: Speichern und Laden von Kamera-Einstellungen pro Kamera
- **Backup-System**: Automatische Sicherung und Wiederherstellung der Original-Parameter
- **Multi-Kamera**: Unterstützung für mehrere angeschlossene Kameras gleichzeitig
- **Startup-Konfiguration**: Automatisches Laden von Einstellungen beim Programmstart
- **Parameter-Tooltips**: Hilfreiche Beschreibungen für alle Parameter
- **Lock-Status**: Visualisierung von gesperrten Parametern
- **Detachable Preview**: Vorschaufenster kann abgetrennt werden
- **CLI-Support**: Kommandozeilenargumente (--minimized, --debug, --version)

### 🛠 Technische Details
- **Programmiersprache**: Python 3.8+ (GLIBC 2.17+ kompatibel)
- **GUI-Framework**: tkinter (systemweit verfügbar)
- **V4L2-Integration**: Direkte v4l2-ctl Befehle für optimale Kompatibilität
- **Konfiguration**: JSON-basierte Speicherung pro Kamera
- **Architektur**: Modularer Aufbau für einfache Wartung
- **Build-System**: GitHub Actions mit PyInstaller
- **Release**: Standalone Linux x86_64 Executable

## 📥 Installation

### Vorkompiliertes Binary (empfohlen)

1. **Neueste Version herunterladen:**
   ```bash
   # Von GitHub Releases
   wget https://github.com/Peschi90/cam-loader-linux/releases/latest/download/CamLoader-linux-x86_64
   chmod +x CamLoader-linux-x86_64
   ```

2. **Anwendung starten:**
   ```bash
   ./CamLoader-linux-x86_64
   
   # Oder minimiert starten:
   ./CamLoader-linux-x86_64 --minimized
   
   # Mit Debug-Logging:
   ./CamLoader-linux-x86_64 --debug
   ```

### Systemanforderungen
- Linux-Distribution mit V4L2-Unterstützung (Ubuntu, Debian, Fedora, Arch, etc.)
- x86_64 Architektur
- GLIBC 2.17 oder höher
- v4l-utils installiert
- Python 3.8+ (für Ausführung aus Quellcode)

### v4l-utils installieren

```bash
# Ubuntu/Debian
sudo apt install v4l-utils

# Fedora
sudo dnf install v4l-utils

# Arch Linux
sudo pacman -S v4l-utils
```

## 🚀 Verwendung

### CLI-Argumente

```bash
# Normal starten
./CamLoader-linux-x86_64

# Minimiert starten (Taskbar/Tray)
./CamLoader-linux-x86_64 --minimized

# Mit Debug-Logging
./CamLoader-linux-x86_64 --debug

# Version anzeigen
./CamLoader-linux-x86_64 --version
```

### Erste Schritte

1. **Anwendung starten** - Verfügbare Kameras werden automatisch erkannt
2. **Kamera auswählen** aus der Dropdown-Liste
3. **Parameter anpassen** mit Schiebereglern und Eingabefeldern
4. **Live-Vorschau starten** mit dem "Start Preview" Button
5. **Einstellungen speichern** - Werden automatisch pro Kamera gespeichert

### Menü-Funktionen

#### File Menu
- **Save Configuration**: Aktuelle Parameter speichern
- **Load Configuration**: Gespeicherte Parameter laden
- **Open Config Folder**: Konfigurationsverzeichnis öffnen
- **Exit**: Anwendung beenden

#### Camera Menu
- **Refresh Cameras**: Kameraliste aktualisieren
- **Backup Parameters**: Original-Parameter sichern
- **Restore Parameters**: Parameter auf Original zurücksetzen
- **Startup Configuration**: Parameter für automatischen Start konfigurieren

#### Help Menu
- **GitHub Repository**: Projekt-Seite öffnen
- **Report Issue**: Bug/Feature-Request auf GitHub erstellen
- **About**: Über-Dialog mit Versionsinformationen
- **Donate**: Projekt mit PayPal unterstützen

### Konfiguration & Backups

**Speicherort:**
- Linux: `~/.camloader/` bzw. `<projekt>/data/configs/`
- Enthält: Kamera-Konfigurationen und Parameter-Backups

**Zugriff:**
- Via Menu: `File → Open Config Folder`
- Via About-Dialog: `📁 Open Config Folder` Button

**Dateien:**
- `<device>_config.json`: Gespeicherte Parameter
- `<device>_backup.json`: Original-Parameter-Backup
- `startup_config.json`: Startup-Konfiguration

### Parameter-Steuerung

Die Anwendung erkennt automatisch alle verfügbaren Kamera-Parameter:

- **Helligkeit** (brightness): Grundhelligkeit des Bildes
- **Kontrast** (contrast): Unterschied zwischen hellen und dunklen Bereichen
- **Sättigung** (saturation): Farbintensität
- **Farbton** (hue): Farbverschiebung
- **Weißabgleich** (white_balance_temperature): Farbtemperatur-Korrektur
- **Belichtung** (exposure_auto, exposure_absolute): Belichtungssteuerung
- **Verstärkung** (gain): Signalverstärkung
- **Schärfe** (sharpness): Bildschärfe
- **Und viele weitere...**

### Backup und Wiederherstellung

1. **Parameter sichern:**
   - Menü "Camera → Backup Parameters" wählen
   - Ursprüngliche Werte werden gespeichert

2. **Parameter wiederherstellen:**
   - Menü "Camera → Restore Parameters" wählen
   - Alle Parameter werden auf Originalwerte zurückgesetzt

### Konfiguration verwalten

1. **Speichern:**
   - Aktueller Zustand wird automatisch beim Beenden gespeichert
   - Manuelles Speichern über "File → Save Configuration"

2. **Laden:**
   - Gespeicherte Einstellungen werden beim Kamera-Wechsel automatisch geladen
   - Import/Export über "File → Load Configuration"

## Entwicklung

### Entwicklungsumgebung einrichten

```bash
# Development-Script verwenden
chmod +x scripts/dev.sh
./scripts/dev.sh setup
```

### Anwendung in Development-Mode starten

```bash
./scripts/dev.sh run
```

### Tests ausführen

```bash
./scripts/dev.sh test
```

### Code formatieren

```bash
./scripts/dev.sh format
```

## 📁 Projektstruktur

```
cam-loader-linux/
├── src/                      # Hauptquellcode
│   ├── main.py              # Einstiegspunkt mit CLI-Args
│   ├── camera/              # Kamera-Steuerung
│   │   ├── __init__.py
│   │   ├── controller.py    # V4L2-Integration
│   │   └── device.py        # Camera-Device-Model
│   ├── gui/                 # Benutzeroberfläche
│   │   ├── __init__.py
│   │   ├── main_window.py   # Hauptfenster
│   │   ├── parameter_frame.py  # Parameter-Controls
│   │   ├── preview_frame.py    # Live-Vorschau
│   │   ├── detached_preview.py # Abtrennbares Vorschaufenster
│   │   └── startup_config.py   # Startup-Config-Dialog
│   ├── config/              # Konfiguration
│   │   ├── __init__.py
│   │   └── manager.py       # Config-Management
│   └── utils/               # Hilfsfunktionen
│       ├── __init__.py
│       └── logger.py        # Logging-Setup
├── data/                    # Konfigurationsdateien
│   └── configs/            # Gespeicherte Kamera-Configs & Backups
├── .github/                # GitHub Actions
│   └── workflows/
│       └── build.yml       # Automated Build Pipeline
├── requirements.txt        # Python-Abhängigkeiten
├── CHANGELOG.md           # Versions-Historie
└── README.md              # Diese Datei
```

## Architektur

### Modularer Aufbau

1. **Camera Module** (`src/camera/`):
   - V4L2-Geräteerkennung
   - Parameter-Management
   - Backup/Restore-Funktionalität

2. **GUI Module** (`src/gui/`):
   - Hauptfenster mit Menüs
   - Parameter-Steuerung mit verschiedenen Widget-Typen
   - Live-Kamera-Vorschau

3. **Config Module** (`src/config/`):
   - JSON-basierte Konfigurationsverwaltung
   - Pro-Kamera Einstellungen
   - Import/Export-Funktionen

4. **Utils Module** (`src/utils/`):
   - Logging-Konfiguration
   - Gemeinsame Hilfsfunktionen

### Datenfluss

```
V4L2-Kameras → CameraController → GUI → ConfigManager
                     ↑                        ↓
               Parameter-Updates          JSON-Dateien
```

## 🐛 Fehlerbehebung

### Häufige Probleme

1. **Keine Kameras gefunden:**
   ```bash
   # Verfügbare Kameras prüfen
   ls /dev/video*
   v4l2-ctl --list-devices
   ```

2. **Permission-Fehler:**
   ```bash
   # Benutzer zur video-Gruppe hinzufügen
   sudo usermod -a -G video $USER
   # Neuanmeldung erforderlich!
   ```

3. **--minimized funktioniert nicht:**
   - Unter Linux: Window Manager muss iconify() unterstützen
   - Testen: `./CamLoader-linux-x86_64 --minimized --debug`
   - Log-Nachricht: "Started in minimized state" sollte erscheinen

4. **OpenCV/Preview-Probleme:**
   ```bash
   # System-Info prüfen
   v4l2-ctl --device=/dev/video0 --list-formats-ext
   ```

5. **Config-Folder nicht gefunden:**
   - Im About-Dialog nachsehen: `Help → About → Config/Backup Location`
   - Oder via Menu: `File → Open Config Folder`

### Debug-Modus

Detaillierte Logs mit Debug-Modus:
```bash
./CamLoader-linux-x86_64 --debug
```

**Wichtige Log-Nachrichten:**
- `"Startup complete - parameter changes will now be applied"` - Init fertig
- `"Started in minimized state"` - Minimierung erfolgreich
- `"Applied startup config for..."` - Startup-Config geladen
- `"Loaded saved config for..."` - Gespeicherte Config geladen

### Support & Issues

🐛 **Bug melden:**
- Via Menu: `Help → Report Issue`
- Oder direkt: [GitHub Issues](https://github.com/Peschi90/cam-loader-linux/issues/new)

📖 **Dokumentation:**
- GitHub Repository: [Peschi90/cam-loader-linux](https://github.com/Peschi90/cam-loader-linux)
- CHANGELOG: Siehe [CHANGELOG.md](CHANGELOG.md)

## 🚧 Bekannte Einschränkungen

- **Nur Linux**: Ausschließlich für Linux-Systeme mit V4L2-Unterstützung
- **Kamera-Unterstützung**: Abhängig von V4L2-Treiber-Qualität
- **Simultane Nutzung**: Kamera kann nicht gleichzeitig von mehreren Anwendungen verwendet werden
- **Window Manager**: Minimized-Start erfordert X11/Wayland Window Manager Unterstützung

## 🗺 Roadmap

### Version 1.0 (Planned)
- [x] ~~Standalone-Binary mit GitHub Actions~~
- [x] ~~CLI-Argumente (--minimized, --debug, --version)~~
- [x] ~~Startup-Konfiguration~~
- [x] ~~Parameter-Lock-Visualisierung~~
- [x] ~~Detachable Preview Window~~
- [x] ~~GitHub Issue Integration~~
- [x] ~~Config-Folder-Zugriff~~

### Future Features
- [ ] Plugin-System für erweiterte Parameter
- [ ] Scripting-Unterstützung für Automatisierung
- [ ] Erweiterte Vorschau-Optionen (Histogramm, Waveform, etc.)
- [ ] Multi-Language-Unterstützung (EN, DE, etc.)
- [ ] Dark Theme / Theme-System
- [ ] Kamera-Profile-Management
- [ ] Batch-Parameter-Export/Import

## 🤝 Beitragen

Beiträge sind willkommen! 

### Wie man beiträgt:

1. Fork des Repositories erstellen
2. Feature-Branch erstellen (`git checkout -b feature/neue-funktion`)
3. Änderungen committen (`git commit -m 'Neue Funktion hinzugefügt'`)
4. Branch pushen (`git push origin feature/neue-funktion`)
5. Pull Request erstellen

### Entwicklung

```bash
# Repository klonen
git clone https://github.com/Peschi90/cam-loader-linux.git
cd cam-loader-linux

# Abhängigkeiten installieren
pip install -r requirements.txt

# Anwendung ausführen
python src/main.py --debug
```

### Coding Standards

- Python PEP 8 Style Guide befolgen
- Docstrings für alle Funktionen und Klassen
- Modularer, testbarer Code
- Aussagekräftige Commit-Messages (Conventional Commits)
- Deutsche Kommentare für User-facing Features

## 💝 Support

### Du findest CamLoader hilfreich?

☕ **Spende via PayPal:** [paypal.me/i3ull3t](https://paypal.me/i3ull3t)

Oder:
- ⭐ Gib dem Projekt einen Star auf GitHub
- 🐛 Melde Bugs und schlage Features vor
- 📖 Verbessere die Dokumentation
- 🔧 Contribue Code

## 📄 Lizenz

MIT License - siehe [LICENSE](LICENSE) Datei für Details.

## 🙏 Danksagungen

- **V4L2-Team**: Für die hervorragende Video4Linux2 API
- **Python Community**: Für tkinter und alle Dependencies
- **OpenCV Project**: Für Video-Funktionalität
- **Alle Contributors**: Danke für eure Unterstützung!

## 📬 Kontakt

- **Developer**: I3uLL3t
- **GitHub**: [@Peschi90](https://github.com/Peschi90)
- **Repository**: [cam-loader-linux](https://github.com/Peschi90/cam-loader-linux)
- **Issues**: [Report Bug/Feature](https://github.com/Peschi90/cam-loader-linux/issues/new)
- **Donate**: [PayPal](https://paypal.me/i3ull3t)

---

**CamLoader** - Einfache und leistungsstarke V4L2-Kamerasteuerung für Linux 🎥✨
