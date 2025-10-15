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

## [0.0.0.16] - 2025-01-15

### Behoben
- **Kritischer Kameraauswahl-Fehler** - StringVar-Fehler komplett behoben mit robuster String-Konvertierung
- **Verbesserte Fehlerbehandlung** - Detaillierter Traceback für bessere Fehlerdiagnose
- **Config-Loading-Schutz** - Zusätzliche Typ-Prüfungen beim Laden von Kamera-Konfigurationen
- **Parse-Error-Behandlung** - Sichere Device-Path-Extraktion mit Try-Catch

### Verbessert
- **Robuste String-Konvertierung** - Explizite str() Konvertierung für alle Kamera-Auswahlen
- **Type-Safe Config-Loading** - isinstance() Prüfungen für alle Config-Zugriffe
- **Detailliertes Error-Logging** - Vollständige Tracebacks für besseres Debugging
- **Sichere Index-Zugriffe** - IndexError und AttributeError werden abgefangen

### Technisch
- Explizite str() Konvertierung in on_camera_selected()
- Try-Catch um device_path split() Operationen
- isinstance() Prüfungen für config, parameters und param_data
- Vollständige traceback.format_exc() in Error-Logs
- Robuste Fehlerbehandlung in allen kritischen Pfaden

### Debugging-Verbesserungen
- **Erweiterte Stack-Traces** - Vollständige Fehlerinformationen im Log
- **Parse-Error-Details** - Genaue Fehlerquelle bei Device-Path-Parsing
- **Type-Validation** - Explizite Typ-Prüfungen vor kritischen Operationen

## [0.0.0.15] - 2025-01-15

### Behoben
- **Slider-Text-Synchronisation** - Texteingabefeld aktualisiert sich jetzt beim Bewegen des Sliders
- **Kameraauswahl-Fehler** - StringVar-Fehler bei der Kameraauswahl behoben
- **Startup-Konfiguration-Dialog** - Tkinter Grab-Fehler beim Öffnen der Kamera-Konfiguration behoben
- **Modal-Dialog-Problem** - Verzögertes grab_set() verhindert "window not viewable" Fehler

### Verbessert
- **Bidirektionale Parameter-Synchronisation** - Slider und Texteingabe sind vollständig synchronisiert
- **Erweiterte Startup-Parameter-Konfiguration** - Bessere Übersicht und Eingabemöglichkeiten
- **Parameter-Anzeige in Startup-Dialog** - Zeigt aktuelle Werte und Bereiche für bessere Orientierung
- **Robuste Kamera-Auswahl** - Bessere Fehlerbehandlung bei ungültigen Auswahlformaten

### Technisch
- Text-Entry-Variablen-Synchronisation zwischen Slider und Eingabefeld
- Verzögertes Modal-Grab für Startup-Konfigurationsdialoge (100ms delay)
- Verbesserte StringVar-Behandlung in Kameraauswahl
- Enhanced Parameter-Kontrollen in Startup-Konfiguration mit Bereichsanzeige
- Automatische Cleanup-Funktionen für Text-Entry-Referenzen

### UI/UX Verbesserungen
- **Startup-Parameter-Dialog** mit aktuellen Werten und Bereichsangaben
- **Slider-Text-Kombination** - Beide Eingabemethoden bleiben synchron
- **Bessere Parameter-Übersicht** in Startup-Konfiguration
- **Robuste Dialog-Behandlung** ohne Grab-Fehler
- **Präzise Werte-Eingabe** mit Slider und Textfeld in Startup-Konfiguration

## [0.0.0.14] - 2025-01-15

### Hinzugefügt
- **Abtrennbares Preview-Fenster** - Preview kann in separates, verschiebbares Fenster ausgelagert werden
- **Neue Layout-Anordnung** - Parameter oberhalb der Vorschau für mehr Platz
- **"Detach Preview" Button** - Preview-Fenster kann von der Hauptanwendung getrennt werden
- **Bewegliches Preview-Fenster** - Vollständig frei positionierbar und größenveränderbar
- **"Attach to Main" Funktion** - Preview-Fenster kann wieder in Hauptanwendung eingebettet werden

### Verbessert
- **Mehr Platz für Parameter** - Vertikale Anordnung gibt Parametern mehr Raum
- **Flexiblere Fenster-Verwaltung** - Preview kann je nach Bedarf angezeigt werden
- **Bessere Arbeitsbereich-Nutzung** - Hauptfenster kann ohne Preview genutzt werden
- **Dynamische Größenanpassung** - Preview-Fenster passt sich an Inhalt an

### Technisch
- DetachedPreviewWindow-Klasse für eigenständiges Preview-Fenster
- Erweiterte PreviewFrame mit Detach/Attach-Funktionalität
- Überarbeitete MainWindow-Layout-Struktur (vertikal statt horizontal)
- Intelligente Preview-State-Übertragung zwischen Fenstern
- Automatische Fenster-Management und Cleanup-Funktionen

### UI/UX Verbesserungen
- Vertikales Haupt-Layout für bessere Parameter-Übersicht
- "Detach Preview" Button in Preview-Kontrollbereich
- Eigenständige Preview-Fenster mit Start/Stop/Attach-Kontrollen
- Anpassbare Fenstergröße und freie Positionierung
- Automatisches Preview-State-Management zwischen Fenstern

## [0.0.0.13] - 2025-01-15

### Hinzugefügt
- **Parameter-Lock-Visualisierung** - Gesperrte Parameter werden mit 🔒 und Status angezeigt
- **Unlock-Funktionalität** - "🔓 Unlock" Button für entsperrbare Parameter
- **Lock-Status-Erkennung** - Automatische Erkennung von read-only und inactive Parametern
- **Visuelle Lock-Unterscheidung** - Verschiedene Icons und Farben für verschiedene Lock-Typen

### Verbessert
- **Parameter-Status-Anzeige** mit farbcodierten Indikatoren:
  - 🔒 (rot) für READ-ONLY Parameter
  - ⚠️ (orange) für INACTIVE Parameter
  - Unlock-Button nur für entsperrbare Parameter
- **Intelligente Unlock-Strategien** - Automatisches Deaktivieren von Auto-Modi
- **Detaillierte Tooltips** für Lock-Status mit Flag-Informationen
- **Parameter-Frame-Layout** für bessere Übersichtlichkeit bei gesperrten Parametern

### Technisch
- Erweiterte V4L2Parameter-Klasse mit is_readonly, is_inactive, flags Properties
- Flag-Parsing in _parse_control_line für v4l2-ctl Output
- try_unlock_parameter() Methode mit Auto-Parameter-Deaktivierung
- get_locking_parameters() für Parameter-Abhängigkeits-Mapping
- Visual Lock-Status-Framework mit Icons und Farbcodierung

### Neue Unlock-Strategien
- **exposure_absolute** ← exposure_auto deaktivieren
- **focus_absolute** ← focus_auto deaktivieren  
- **white_balance_temperature** ← white_balance_temperature_auto deaktivieren
- **gain** ← gain_automatic deaktivieren
- **brightness/contrast/saturation** ← auto_exposure deaktivieren

### UI/UX Verbesserungen
- Deaktivierte Kontrollen für gesperrte Parameter
- Unlock-Hilfe mit aktuellen Werten der sperrenden Parameter
- Erfolgs-/Fehlermeldungen für Unlock-Versuche
- Automatische Parameter-Refresh nach erfolgreichem Unlock

## [0.0.0.12] - 2025-01-15

### Hinzugefügt
- **Erweiterte Kamera-Erkennung** - Überprüfung ob Kameras Preview-fähig sind
- **Text-Eingabefelder** für direkte Werteingabe neben Schiebereglern
- **Parameter-Tooltips** mit englischen Erklärungen für alle Kamera-Parameter
- **Startup-Konfiguration-Menü** zur Auswahl welche Kameras beim Start konfiguriert werden
- **Nicht-funktionale Kamera-Kennzeichnung** mit "[No Preview]" Markierung

### Verbessert
- **Kamera-Erkennung** prüft jetzt v4l2-ctl --list-formats für tatsächliche Funktionalität
- **Parameter-Kontrollen** mit kombinierten Schieberegler + Texteingabe
- **Benutzerfreundlichkeit** durch informative Tooltips mit Parameterbeschreibungen
- **Automatische Konfiguration** beim Anwendungsstart für definierte Kameras

### Technisch
- Neue Hilfsmethoden: _is_capture_device(), _check_preview_capability()
- Parameter-Tooltip-System mit umfangreicher Beschreibungsdatenbank
- StartupConfigWindow für grafische Konfigurationsverwaltung
- Erweiterte Kamera-Verfügbarkeitsprüfungen
- JSON-basierte Startup-Konfigurationsspeicherung

### Neue Features
- **Startup Configuration Dialog** - Vollständige GUI für Kamera-Startup-Einstellungen
- **Parameter Range Validation** - Automatische Wertebereichsprüfung in Texteingaben
- **Camera Capability Detection** - Unterscheidung zwischen existierenden und funktionalen Kameras
- **Enhanced Tooltips** - Über 30 detaillierte Parameter-Erklärungen in englischer Sprache

## [0.0.0.11] - 2025-01-15

### Behoben
- **Python-Version-Problem** - Build verwendete immer noch Python 3.11 statt 3.8
- **GLIBC 2.38 Abhängigkeit** durch Downgrade auf Python 3.8 eliminiert
- **Explizite Python-Interpreter-Verwendung** in allen Build-Schritten
- **PyInstaller Python-Version-Verifikation** hinzugefügt

### Geändert
- **Python-Version** von 3.9 auf 3.8 reduziert für maximale Kompatibilität
- **Konsistente Python-Verwendung** (python statt python3) im gesamten Workflow
- **Build-Logging** erweitert um Python-Version-Informationen
- **Explizite Pfad-Verifikation** für Python-Interpreter

### Technisch
- Python 3.8 hat deutlich niedrigere GLIBC-Anforderungen
- Konsistente Verwendung des setup-python konfigurierten Interpreters
- Verbesserte Debug-Ausgaben für Python-Version-Tracking

## [0.0.0.10] - 2025-01-15

### Behoben
- **Container GLIBC-Problem** gelöst durch Rückkehr zu Standard Ubuntu 22.04 Runner
- **GitHub Actions Node.js Kompatibilität** - Ubuntu 18.04 Container nicht mit Actions kompatibel
- **Mehrschichtige Kompatibilitätsstrategie** implementiert (staticx → AppImage → Standard)
- **AppImage-Unterstützung** für maximale Linux-Distribution-Kompatibilität hinzugefügt

### Hinzugefügt
- **Staticx-Integration** für statische Verlinkung als primäre Lösung
- **AppImage-Fallback** für Situationen wo staticx nicht funktioniert
- **Erweiterte Compatibility-Pipeline** mit mehreren Fallback-Strategien
- **AppImage-Tools** Installation für portable Anwendungen

### Geändert
- **Build-Strategie** von Container-basiert zu Multi-Fallback-Ansatz
- **Kompatibilitäts-Layer** mit drei verschiedenen Ansätzen
- **Bessere Fehlerbehandlung** bei Build-Problemen

### Technisch
- Standard Ubuntu 22.04 Runner mit modernen GitHub Actions
- Fallback-Kette: staticx → AppImage → Standard PyInstaller
- AppImage für universelle Linux-Kompatibilität
- Automatische Erkennung der besten verfügbaren Methode

## [0.0.0.9] - 2025-01-15

### Behoben
- **Ubuntu 20.04 Runner-Problem** gelöst durch Verwendung von Ubuntu 18.04 Container
- **GLIBC-Kompatibilität** verbessert durch ältere Build-Umgebung (GLIBC 2.27)
- **Statische Verlinkung** mit staticx für bessere Portabilität hinzugefügt
- **Build-Umgebung** korrigiert für verfügbare GitHub Actions Runner

### Geändert
- **Container-basiertes Build** mit Ubuntu 18.04 für maximale Kompatibilität
- **Python 3.9** Installation aus deadsnakes PPA
- **Staticx-Integration** für statisch verlinkte Binaries
- **Erweiterte Dependency-Installation** für ältere Ubuntu-Basis

### Technisch
- Ubuntu 18.04 Container mit GLIBC 2.27 (kompatibel mit Debian 9+)
- Fallback auf statische Verlinkung wenn verfügbar
- Verbesserte Package-Installation für Container-Umgebung

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