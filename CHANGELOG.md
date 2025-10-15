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

## [0.0.0.8] - 2025-01-15

### Behoben
- **GLIBC-Kompatibilitätsproblem** gelöst durch Verwendung von Ubuntu 20.04 und Python 3.9
- **"GLIBC_2.38 not found" Fehler** behoben für ältere Debian/Ubuntu-Systeme
- **Bessere Systemkompatibilität** durch ältere Build-Umgebung
- **Erweiterte GLIBC-Checks** im Debug-Wrapper hinzugefügt

### Geändert
- **Build-Umgebung** von Ubuntu-latest auf Ubuntu 20.04 geändert
- **Python-Version** von 3.11 auf 3.9 reduziert für bessere Kompatibilität
- **Debug-Logging** in PyInstaller aktiviert
- **Erweiterte System-Informationen** im Debug-Wrapper

### Technisch
- Ubuntu 20.04 verwendet GLIBC 2.31 (kompatibel mit Debian 10+)
- Python 3.9 hat niedrigere Systemanforderungen als 3.11
- Verbesserte Kompatibilitätsprüfungen vor Release

## [0.0.0.7] - 2025-01-15

### Behoben
- **Debian/Ubuntu Kompatibilität** verbessert für ausführbare Datei
- **PyInstaller-Konfiguration** mit erweiterten tkinter und OpenCV Abhängigkeiten
- **Debug-Modus aktiviert** mit Console-Output für bessere Fehlerdiagnose
- **Debug-Wrapper-Script** für Troubleshooting hinzugefügt

### Hinzugefügt
- **TROUBLESHOOTING.md** mit umfangreicher Anleitung für Debian-Systeme
- **Debug-Script** (`camloader-debug.sh`) für Systemanalyse
- **Erweiterte Abhängigkeits-Checks** im Build-Prozess
- **Bessere Fehlerbehandlung** mit detaillierteren Logs

### Technisch
- Console-Modus aktiviert (`console=True`) für Debug-Ausgaben
- Zusätzliche tkinter-Module für bessere GUI-Kompatibilität
- Ausgeschlossene große Bibliotheken (matplotlib, scipy) für kleinere Dateigröße
- Verbesserte Library-Dependency-Checks

## [0.0.0.6] - 2025-01-15

### Behoben
- **YAML-Syntax-Fehler** in GitHub Actions Workflow behoben
- **Workflow vereinfacht** - erstellt nur noch einzelne ausführbare Datei und Quellcode-Pakete
- **Einrückungsfehler** in mehrzeiligen YAML-Strings korrigiert
- **Release-Pipeline** optimiert für einfachere Bereitstellung ohne komplexe Installationsskripte

### Technisch
- YAML-Syntax-Validierung mit PyYAML hinzugefügt
- Workflow-Architektur vereinfacht (entfernte komplexe Packaging-Skripte)
- Direkte ausführbare Dateien ohne Installation per Doppelklick nutzbar

## [0.0.0.5] - 2025-10-15

### Behoben
- **Release Notes** werden jetzt korrekt aus CHANGELOG.md extrahiert und in GitHub Releases angezeigt
- **Workflow-Verbesserung** mit robustem Changelog-Parsing und besserer Fehlerbehandlung
- **Debugging** für Release-Erstellung hinzugefügt

### Technisch
- Changelog-Parsing von Regex auf manuelle Zeilenverarbeitung umgestellt
- Bessere Behandlung von gemischten deutschen/englischen Inhalten
- Fallback-Content für fehlende oder leere Changelog-Abschnitte

## [0.0.0.4] - 2025-10-15

### Fixed
- Added .gitkeep file to preserve data directory structure for PyInstaller builds
- Ensured data directory is properly included in Git repository
- Fixed PyInstaller build failing due to missing data directory

## [0.0.0.3] - 2025-10-15

### Behoben
- **PyInstaller Build-Fehler** durch fehlenden data-Ordner
- **Workflow-Optimierung** mit reduzierten System-Dependencies für schnellere Builds
- **Conditional Data Directory** Inclusion für robustere Spec-File-Generierung

### Technisch
- Spec-File jetzt mit OS-Überprüfung für data-Verzeichnis
- Vereinfachte apt-get Installationen (nur notwendige Pakete)
- Verbesserte Fehlerbehandlung im Build-Prozess

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