# CamLoader - V4L2 Camera Parameter Controller

Eine benutzerfreundliche GUI-Anwendung zur Steuerung von V4L2-Kamera-Parametern unter Linux, entwickelt als Alternative zu gucview mit Fokus auf Einfachheit und Wartbarkeit.

## Features

### 🎯 Hauptfunktionen
- **Kamera-Erkennung**: Automatische Erkennung aller verfügbaren V4L2-Kameras
- **Parameter-Steuerung**: Intuitive Bedienelemente für alle Kamera-Parameter (Helligkeit, Kontrast, Sättigung, etc.)
- **Live-Vorschau**: Echtzeit-Kamera-Preview mit konfigurierbarer Auflösung
- **Konfiguration**: Speichern und Laden von Kamera-Einstellungen
- **Backup-System**: Sicherung und Wiederherstellung der Original-Parameter
- **Multi-Kamera**: Unterstützung für mehrere angeschlossene Kameras

### 🛠 Technische Details
- **Programmiersprache**: Python 3.8+
- **GUI-Framework**: tkinter (systemweit verfügbar)
- **V4L2-Integration**: Direkte v4l2-ctl Befehle für optimale Kompatibilität
- **Konfiguration**: JSON-basierte Speicherung
- **Architektur**: Modularer Aufbau für einfache Wartung

## Installation

### Systemanforderungen
- Linux-Distribution mit V4L2-Unterstützung
- Python 3.8 oder höher
- v4l-utils Paket
- tkinter (meist vorinstalliert)

### Automatische Installation

1. **Repository klonen:**
```bash
git clone https://github.com/yourusername/cam-loader-linux.git
cd cam-loader-linux
```

2. **Build-Script ausführen:**
```bash
chmod +x scripts/build.sh
./scripts/build.sh
```

3. **Anwendung starten:**
```bash
./dist/camloader.sh
```

### Manuelle Installation

1. **Abhängigkeiten installieren:**
```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip python3-tkinter v4l-utils

# Fedora
sudo dnf install python3 python3-pip python3-tkinter v4l-utils

# Arch Linux
sudo pacman -S python python-pip tk v4l-utils
```

2. **Python-Umgebung einrichten:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Anwendung starten:**
```bash
python src/main.py
```

## Verwendung

### Erste Schritte

1. **Anwendung starten** und verfügbare Kameras werden automatisch erkannt
2. **Kamera auswählen** aus der Dropdown-Liste
3. **Parameter anpassen** mit den Schiebereglern und Eingabefeldern
4. **Live-Vorschau starten** mit dem "Start Preview" Button
5. **Einstellungen speichern** über das Menü "File → Save Configuration"

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

## Projektstruktur

```
cam-loader-linux/
├── src/                    # Hauptquellcode
│   ├── main.py            # Einstiegspunkt
│   ├── camera/            # Kamera-Steuerung
│   │   ├── __init__.py
│   │   └── controller.py  # V4L2-Integration
│   ├── gui/               # Benutzeroberfläche
│   │   ├── __init__.py
│   │   ├── main_window.py # Hauptfenster
│   │   ├── parameter_frame.py # Parameter-Controls
│   │   └── preview_frame.py   # Live-Vorschau
│   ├── config/            # Konfiguration
│   │   ├── __init__.py
│   │   └── manager.py     # Config-Management
│   └── utils/             # Hilfsfunktionen
│       ├── __init__.py
│       └── logger.py      # Logging-Setup
├── data/                  # Konfigurationsdateien
│   └── configs/          # Gespeicherte Kamera-Configs
├── scripts/              # Build- und Dev-Scripts
│   ├── build.sh         # Haupt-Build-Script
│   └── dev.sh           # Development-Utilities
├── requirements.txt      # Python-Abhängigkeiten
├── setup.py             # Installationsskript
└── README.md            # Diese Datei
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

## Fehlerbehebung

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
   # Neuanmeldung erforderlich
   ```

3. **Tkinter nicht verfügbar:**
   ```bash
   # Ubuntu/Debian
   sudo apt install python3-tkinter
   
   # Fedora
   sudo dnf install python3-tkinter
   ```

4. **OpenCV-Probleme:**
   ```bash
   # Alternative OpenCV-Installation
   pip install opencv-python-headless
   ```

### Logging

Detaillierte Logs sind verfügbar:
```bash
# Mit Debug-Logging starten
PYTHONPATH=src python main.py --log-level DEBUG
```

## Bekannte Einschränkungen

- **Nur Linux**: Ausschließlich für Linux-Systeme mit V4L2-Unterstützung
- **Kamera-Unterstützung**: Abhängig von V4L2-Treiber-Qualität
- **Simultane Nutzung**: Kamera kann nicht gleichzeitig von mehreren Anwendungen verwendet werden

## Roadmap

### Geplante Features
- [ ] Plugin-System für erweiterte Parameter
- [ ] Scripting-Unterstützung für Automatisierung
- [ ] Erweiterte Vorschau-Optionen (Histogramm, etc.)
- [ ] Multi-Language-Unterstützung
- [ ] Dark Theme

### Verbesserungen
- [ ] Performance-Optimierung der Live-Vorschau
- [ ] Erweiterte Kamera-Profile
- [ ] Batch-Parameter-Änderungen
- [ ] Kommandozeilen-Interface

## Beitragen

Beiträge sind willkommen! Bitte:

1. Fork des Repositories erstellen
2. Feature-Branch erstellen (`git checkout -b feature/neue-funktion`)
3. Änderungen committen (`git commit -m 'Neue Funktion hinzugefügt'`)
4. Branch pushen (`git push origin feature/neue-funktion`)
5. Pull Request erstellen

### Coding Standards

- Python PEP 8 Style Guide befolgen
- Docstrings für alle Funktionen und Klassen
- Modularer, testbarer Code
- Aussagekräftige Commit-Messages

## Lizenz

MIT License - siehe [LICENSE](LICENSE) Datei für Details.

## Support

- **Issues**: GitHub Issues für Bug-Reports und Feature-Requests
- **Diskussionen**: GitHub Discussions für allgemeine Fragen
- **E-Mail**: your.email@example.com

## Danksagungen

- V4L2-Entwicklerteam für die hervorragende API
- Python tkinter-Community
- OpenCV-Projekt für Video-Funktionalität
- Alle Mitwirkenden und Tester

---

**CamLoader** - Einfache und leistungsstarke V4L2-Kamerasteuerung für Linux
