# Changelog

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Geplant
- Plugin-System für erweiterte Parameter
- Scripting-Unterstützung für Automatisierung
- Erweiterte Vorschau-Optionen (Histogramm, etc.)
- Multi-Language-Unterstützung
- Dark Theme

## [0.0.0.2] - 2025-10-15

### Verbessert
- **GitHub Actions Workflow** komplett überarbeitet für bessere Zuverlässigkeit
- **Build-System** mit moderneren GitHub Actions und robusteren Pfad-Behandlung
- **PyInstaller-Konfiguration** für optimierte Linux-Builds
- **Package-Erstellung** mit automatischen Install-Scripts und Desktop-Integration
- **Changelog-Extraktion** mit verbesserter Fehlerbehandlung

### Behoben
- Hardcodierte Datei-Pfade in GitHub Actions Workflow
- Deprecated GitHub Actions durch moderne Versionen ersetzt
- Robuste Artefakt-Erkennung für dynamische Dateinamen
- Upload-Fehler bei Release-Assets durch bessere Pfad-Auflösung

### Technisch
- Verwendung von `softprops/action-gh-release@v2` statt deprecated Actions
- Dynamische Paket-Erkennung in Build-Pipeline
- Verbesserter Xvfb-Setup für headless GUI-Builds
- Separate Jobs für bessere Fehler-Isolation

## [0.0.0.1] - 2025-10-15

### Hinzugefügt
- **GUI-Anwendung** mit tkinter für benutzerfreundliche Bedienung
- **Automatische Kamera-Erkennung** aller verfügbaren V4L2-Geräte
- **Parameter-Steuerung** mit intuitiven Schiebereglern und Eingabefeldern
  - Helligkeit (brightness)
  - Kontrast (contrast) 
  - Sättigung (saturation)
  - Farbton (hue)
  - Weißabgleich (white_balance_temperature)
  - Belichtung (exposure_auto, exposure_absolute)
  - Verstärkung (gain)
  - Schärfe (sharpness)
  - Und alle anderen verfügbaren V4L2-Parameter
- **Live-Kamera-Vorschau** mit OpenCV-Integration
  - Einstellbare Auflösung
  - Echtzeit-Parameter-Updates
  - Thread-basierte Performance
- **Konfigurationssystem** für persistente Einstellungen
  - JSON-basierte Speicherung pro Kamera
  - Automatisches Laden beim Kamera-Wechsel
  - Import/Export von Konfigurationen
- **Backup-System** für Original-Parameter
  - Sicherung der ursprünglichen Kamera-Einstellungen
  - Ein-Klick-Wiederherstellung
  - Schutz vor versehentlichen Änderungen
- **Multi-Kamera-Unterstützung**
  - Dropdown-Auswahl zwischen Kameras
  - Separate Konfigurationen pro Gerät
  - Hot-Swap-fähig
- **Modulare Architektur** für einfache Wartung
  - Getrennte Module für Camera, GUI, Config, Utils
  - Saubere Schnittstellen zwischen Komponenten
  - Erweiterbare Struktur

### Technische Features
- **V4L2-Integration** über direkte v4l2-ctl Befehle
- **Cross-Platform-Kompatibilität** (Entwicklung unter Windows möglich)
- **Logging-System** mit konfigurierbaren Log-Levels
- **Error-Handling** mit benutzerfreundlichen Fehlermeldungen
- **Threading** für nicht-blockierende GUI-Operations

### Build-System
- **Automatisierte Build-Scripts** für Linux-Deployment
- **Development-Tools** für einfache Entwicklung
- **PyInstaller-Integration** für standalone Executables
- **Requirements-Management** mit pip
- **Desktop-Integration** mit .desktop-Dateien

### Dokumentation
- **Umfassende README** mit Installation und Nutzung
- **Code-Dokumentation** mit Docstrings
- **Beispiele** und Troubleshooting-Guide
- **Architektur-Übersicht** für Entwickler

## [0.1.0] - 2025-10-15

### Hinzugefügt
- Initiales Projekt-Setup
- Grundlegende Projektstruktur
- Erste Entwicklungsversion

---

## Changelog-Format

### Kategorien
- **Hinzugefügt** für neue Features
- **Geändert** für Änderungen an bestehender Funktionalität
- **Veraltet** für Features, die bald entfernt werden
- **Entfernt** für Features, die in dieser Version entfernt wurden
- **Behoben** für Bugfixes
- **Sicherheit** bei Sicherheitsupdates

### Versionierung
- **MAJOR** Version bei inkompatiblen API-Änderungen
- **MINOR** Version bei neuer Funktionalität (rückwärtskompatibel)
- **PATCH** Version bei Bugfixes (rückwärtskompatibel)

### Beispiel für zukünftige Releases

```markdown
## [1.1.0] - YYYY-MM-DD

### Hinzugefügt
- Neue Parameter-Profile für verschiedene Anwendungsfälle
- Batch-Verarbeitung für mehrere Kameras
- Keyboard-Shortcuts für häufige Aktionen

### Geändert
- Verbesserte Performance der Live-Vorschau
- Überarbeitete Benutzeroberfläche für bessere Usability

### Behoben
- Problem mit Kamera-Erkennung bei USB-Hub-Verbindungen
- Memory-Leak in der Preview-Funktion
- Fehlerhafte Parameter-Validierung bei extremen Werten
```