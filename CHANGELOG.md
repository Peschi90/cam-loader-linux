# Changelog# Changelog# Changelog



All notable changes to this project will be documented in this file.



The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),All notable changes to this project will be documented in this file.Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).



## [Unreleased]

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),

### Planned

- Plugin system for extended parametersand this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).und dieses Projekt folgt [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

- Scripting support for automation

- Extended preview options (histogram, etc.)

- Multi-language support

- Dark theme## [Unreleased]## [Unreleased]



## [0.0.0.24] - 2025-10-16



### Changed### Planned### Geplant

- **Complete English Translation** - All documentation now in English

- **README.md** - Fully translated to English- Plugin system for extended parameters- Plugin-System für erweiterte Parameter

- **CHANGELOG.md** - Completely translated to English  

- **TROUBLESHOOTING.md** - Translated to English- Scripting support for automation- Scripting-Unterstützung für Automatisierung

- **International Audience** - Better accessibility for non-German speakers

- Extended preview options (histogram, etc.)- Erweiterte Vorschau-Optionen (Histogramm, etc.)

### Improved

- **Documentation Quality** - Professional English documentation- Multi-language support- Multi-Language-Unterstützung

- **Global Reach** - Project now accessible to international developers

- **Contribution Guidelines** - English coding standards for international contributors- Dark theme- Dark Theme

- **Issue Reporting** - English documentation for better GitHub issue quality



### Technical

- Maintained all technical content accuracy during translation## [0.0.0.23] - 2025-10-15## [0.0.0.23] - 2025-10-15

- Preserved all code examples and commands

- Kept all links and references intact

- Updated contact and contribution sections

### Added### Hinzugefügt

## [0.0.0.23] - 2025-10-15

- **📖 GitHub Repository Link** - Direct link in Help menu- **📖 GitHub Repository Link** - Direkter Link im Help-Menu

### Added

- **📖 GitHub Repository Link** - Direct link in Help menu- **🐛 Report Issue** - Create GitHub issue directly from application- **🐛 Report Issue** - GitHub Issue direkt aus Anwendung erstellen

- **🐛 Report Issue** - Create GitHub issue directly from application

- **📁 Open Config Folder** - Open configuration directory (File menu)- **📁 Open Config Folder** - Open configuration directory (File menu)- **📁 Open Config Folder** - Konfigurationsverzeichnis öffnen (File-Menu)

- **Enhanced About Dialog** - Larger (600x650) with scrollbar

- **Config Path Display** - Backup/config storage location visible in About dialog- **Enhanced About Dialog** - Larger (600x650) with scrollbar- **Erweiterter About-Dialog** - Größer (600x650) mit Scrollbar

- **Clickable Links** - GitHub link clickable in About dialog

- **Modal About Dialog** - grab_set() for better UX- **Config Path Display** - Backup/config storage location visible in About dialog- **Config-Pfad-Anzeige** - Backup/Config-Speicherort im About-Dialog sichtbar



### Improved- **Clickable Links** - GitHub link clickable in About dialog- **Klickbare Links** - GitHub-Link im About-Dialog klickbar

- **About Dialog** - Enlarged from 500x400 to 600x650

- **Developer Info** - Better readability with more spacing- **Modal About Dialog** - grab_set() for better UX- **Modal About-Dialog** - grab_set() für bessere UX

- **Feature List** - Complete with all 10 features

- **Menu Structure** - GitHub & issue links in Help menu

- **README.md** - Completely revised with all new features

### Improved### Verbessert

### Technical

- `open_github_repo()` - Opens repository in browser- **About Dialog** - Enlarged from 500x400 to 600x650- **About-Dialog** - Von 500x400 auf 600x650 vergrößert

- `open_github_issue()` - Opens GitHub issue page

- `open_config_folder()` - Platform-agnostic (Linux/Windows/macOS)- **Developer Info** - Better readability with more spacing- **Developer-Infos** - Besser lesbar mit mehr Abständen

- Scrollable About dialog with Canvas

- Centered dialog positioning- **Feature List** - Complete with all 10 features- **Feature-Liste** - Vollständig mit allen 10 Features



### UX Improvements- **Menu Structure** - GitHub & issue links in Help menu- **Menu-Struktur** - GitHub & Issue-Links im Help-Menu

- **Access to Configs**: Now 2 ways (File menu + About dialog)

- **Bug Reporting**: 1-click GitHub issue creation- **README.md** - Completely revised with all new features- **README.md** - Komplett überarbeitet mit allen neuen Features

- **Transparency**: Config storage location always visible

- **Help**: Direct access to repository and documentation  - CLI arguments documented  - CLI-Argumente dokumentiert



## [0.0.0.22] - 2025-10-15  - Menu functions explained  - Menu-Funktionen erklärt



### Fixed  - Config storage location described  - Config-Speicherort beschrieben

- **--minimized on Linux** - Now works correctly with X11/Wayland window managers

- **update_idletasks()** - Forces tkinter to communicate with window manager  - Debug information added  - Debug-Informationen hinzugefügt

- **Timing Issue** - deiconify() → update → iconify() sequence for Linux

  - Support links updated  - Support-Links aktualisiert

### Improved

- **Platform-agnostic** - Now works on both Windows AND Linux  - Roadmap with completed features  - Roadmap mit erledigten Features

- **Debug Logging** - "Started in minimized state" message added

- **start_minimized Flag** - Stored as instance variable for later access



### Technical### Technical### Technisch

- `self.start_minimized` stored in __init__

- `update_idletasks()` before and after `deiconify()` for Linux window manager sync- `open_github_repo()` - Opens repository in browser- `open_github_repo()` - Öffnet Repository in Browser

- Minimization occurs after complete UI setup

- `open_github_issue()` - Opens GitHub issue page- `open_github_issue()` - Öffnet GitHub Issue-Seite

## [0.0.0.21] - 2025-10-15

- `open_config_folder()` - Platform-agnostic (Linux/Windows/macOS)- `open_config_folder()` - Platform-agnostisch (Linux/Windows/macOS)

### Fixed

- **--minimized CLI Argument** - Application now starts correctly minimized- Scrollable About dialog with Canvas- Scrollbarer About-Dialog mit Canvas

- **Window Visibility** - window.withdraw() directly after window creation

- **Startup Flow** - Minimized logic moved before UI setup- Centered dialog positioning- Zentrierte Dialog-Positionierung



### Technical

- `withdraw()` directly after `tk.Tk()` creation with --minimized flag

- `deiconify()` + `iconify()` at end for correct minimization### UX Improvements### UX-Verbesserungen

- Prevents brief window flash when starting minimized

- **Access to Configs**: Now 2 ways (File menu + About dialog)- **Zugriff auf Configs**: Jetzt 2 Wege (File-Menu + About-Dialog)

## [0.0.0.20] - 2025-01-15

- **Bug Reporting**: 1-click GitHub issue creation- **Bug-Reporting**: 1-Klick GitHub Issue erstellen

### Fixed

- **Duplicate Parameter Setting at Startup** - Parameters no longer set multiple times- **Transparency**: Config storage location always visible- **Transparenz**: Config-Speicherort immer sichtbar

- **Unnecessary Parameter Transfers** - No automatic sets outside startup config

- **Startup Flow Optimized** - Only startup config sets parameters at start- **Help**: Direct access to repository and documentation- **Hilfe**: Direkter Zugang zu Repository und Dokumentation



### Improved

- **Startup Flag** - startup_complete flag prevents parameter sets during initialization

- **load_camera_config** - Now only display refresh, no parameter transfer## [0.0.0.22] - 2025-10-15## [0.0.0.22] - 2025-10-15

- **Clear Startup Flow** - Only startup configuration writes parameters at start

- **Logging Clarity** - "Startup complete" message marks end of initialization



### Technical### Fixed### Behoben

- startup_complete flag in MainWindow.__init__()

- load_camera_config() checks startup_complete before execution- **--minimized on Linux** - Now works correctly with X11/Wayland window managers- **--minimized unter Linux** - Funktioniert jetzt korrekt mit X11/Wayland Window Managern

- Removed parameter-setting loop from load_camera_config()

- Debug logging for skipped config loads during startup- **update_idletasks()** - Forces tkinter to communicate with window manager- **update_idletasks()** - Zwingt tkinter zur Kommunikation mit Window Manager



### Behavior Changes- **Timing Issue** - deiconify() → update → iconify() sequence for Linux- **Timing-Problem** - deiconify() → update → iconify() Sequenz für Linux

**BEFORE this change:**

1. Camera detection → set parameters

2. Load config → set parameters

3. Startup config → set parameters### Improved### Verbessert

4. Select first camera → set parameters

= Parameters set 3-4 times!- **Platform-agnostic** - Now works on both Windows AND Linux- **Platform-agnostisch** - Funktioniert jetzt auf Windows UND Linux



**AFTER this change:**- **Debug Logging** - "Started in minimized state" message added- **Debug-Logging** - "Started in minimized state" Nachricht hinzugefügt

1. Camera detection → only load

2. Load config → skipped (startup_complete=False)- **start_minimized Flag** - Stored as instance variable for later access- **start_minimized Flag** - Als Instanz-Variable gespeichert für späteren Zugriff

3. Startup config → set parameters (only source at start)

4. startup_complete = True

5. Select first camera → only display refresh

= Parameters set 1 time!### Technical### Technisch



### Logging Improvements- `self.start_minimized` stored in __init__- `self.start_minimized` in __init__ gespeichert

- "Startup complete - parameter changes will now be applied"

- "Skipping config load for /dev/videoX - startup not complete" (DEBUG)- `update_idletasks()` before and after `deiconify()` for Linux window manager sync- `update_idletasks()` vor und nach `deiconify()` für Linux Window Manager Sync

- "Loaded saved config for /dev/videoX, refreshing display only"

- Minimization occurs after complete UI setup- Minimierung erfolgt nach vollständigem UI-Setup

## [0.0.0.19] - 2025-01-15



### Added

- **CLI Arguments** - Command line support for various startup options## [0.0.0.21] - 2025-10-15## [0.0.0.21] - 2025-10-15

- **Minimized Start** - `--minimized` or `-m` starts application minimized

- **Debug Mode** - `--debug` enables debug logging

- **Version Display** - `--version` shows version, also visible in window title

- **Enhanced About Dialog** - Shows author (I3uLL3t), features and version### Fixed### Behoben

- **Donation Button** - PayPal.me/i3ull3t link in About dialog and Help menu

- **Detailed Startup Logging** - Device path in all startup config logs- **--minimized CLI Argument** - Application now starts correctly minimized- **--minimized CLI Argument** - Anwendung startet jetzt korrekt minimiert



### CLI Usage- **Window Visibility** - window.withdraw() directly after window creation- **Fenster-Sichtbarkeit** - window.withdraw() direkt nach Fenster-Erstellung

```bash

# Start normally- **Startup Flow** - Minimized logic moved before UI setup- **Startup-Flow** - Minimized-Logik vor UI-Setup verschoben

python src/main.py



# Start minimized

python src/main.py --minimized### Technical### Technisch



# With debug logging- `withdraw()` directly after `tk.Tk()` creation with --minimized flag- `withdraw()` direkt nach `tk.Tk()` Erstellung bei --minimized Flag

python src/main.py --debug

- `deiconify()` + `iconify()` at end for correct minimization- `deiconify()` + `iconify()` am Ende für korrekte Minimierung

# Show version

python src/main.py --version- Prevents brief window flash when starting minimized- Verhindert kurzes Aufblitzen des Fensters bei minimiertem Start

```



## [0.0.0.18] - 2025-01-15

## [0.0.0.20] - 2025-01-15## [0.0.0.20] - 2025-01-15

### Fixed

- **Slider-Text Synchronization** - Text input field now updates correctly when moving slider

- **Preview Camera Switch** - Preview automatically switches to new camera when active

- **Detached Preview Camera Switch** - Detached preview also follows camera switch### Fixed### Behoben

- **Messagebox Foreground** - Messageboxes and dialogs now always appear in foreground

- **Duplicate Parameter Setting at Startup** - Parameters no longer set multiple times- **Doppeltes Parameter-Setzen beim Start** - Parameter werden nicht mehr mehrfach gesetzt

### Improved

- **Automatic Preview Restart** - Preview automatically restarts on camera switch if running- **Unnecessary Parameter Transfers** - No automatic sets outside startup config- **Unnötige Parameter-Übertragungen** - Keine automatischen Sets außerhalb Startup-Config

- **Dialog Focus Management** - lift() and focus_force() for all dialogs

- **Text Entry Initialization** - _text_entry_vars initialized before slider creation- **Startup Flow Optimized** - Only startup config sets parameters at start- **Startup-Flow optimiert** - Nur Startup-Config setzt Parameter beim Start

- **Robust Camera Updates** - Synchronized updates for all preview windows



## [0.0.0.17] - 2025-01-15

### Improved### Verbessert

### Fixed

- **Critical Parameter Frame Error** - StringVar in parameter_widgets caused crashes on camera switch- **Startup Flag** - startup_complete flag prevents parameter sets during initialization- **Startup-Flag** - startup_complete Flag verhindert Parameter-Sets während Initialisierung

- **Camera Switch Now Works** - Fully functional switching between cameras

- **Preview Problems Fixed** - Preview now works correctly after camera switch- **load_camera_config** - Now only display refresh, no parameter transfer- **load_camera_config** - Nur noch Display-Refresh, keine Parameter-Übertragung

- **Widget Cleanup Error** - Robust error handling when cleaning up parameter widgets

- **Clear Startup Flow** - Only startup configuration writes parameters at start- **Klarer Startup-Flow** - Nur Startup-Configuration schreibt Parameter beim Start

### Improved

- **Robust Widget Management** - Type checking before accessing widget_info dictionary- **Logging Clarity** - "Startup complete" message marks end of initialization- **Logging-Klarheit** - "Startup complete" Nachricht markiert Ende der Initialisierung

- **Safe Widget Destruction** - Try-catch around all destroy() calls

- **Better Error Handling** - Warning instead of crash on unexpected widget type

- **Clean Data Structure** - No more StringVars directly in parameter_widgets

### Technical### Technisch

## [0.0.0.14] - 2025-01-15

- startup_complete flag in MainWindow.__init__()- startup_complete Flag in MainWindow.__init__()

### Added

- **Detachable Preview Window** - Preview can be moved to separate, movable window- load_camera_config() checks startup_complete before execution- load_camera_config() prüft startup_complete vor Ausführung

- **New Layout Arrangement** - Parameters above preview for more space

- **"Detach Preview" Button** - Preview window can be detached from main application- Removed parameter-setting loop from load_camera_config()- Entfernte Parameter-Setting-Schleife aus load_camera_config()

- **Movable Preview Window** - Fully freely positionable and resizable

- **"Attach to Main" Function** - Preview window can be embedded back into main application- Debug logging for skipped config loads during startup- Debug-Logging für übersprungene Config-Loads während Startup



### Technical

- DetachedPreviewWindow class for standalone preview window

- Extended PreviewFrame with detach/attach functionality### Behavior Changes### Behavior Changes

- Revised MainWindow layout structure (vertical instead of horizontal)

- Intelligent preview state transfer between windows**BEFORE this change:****VOR dieser Änderung:**

- Automatic window management and cleanup functions

1. Camera detection → set parameters1. Kamera-Erkennung → Parameter setzen

## [0.0.0.13] - 2025-01-15

2. Load config → set parameters2. Config laden → Parameter setzen

### Added

- **Parameter Lock Visualization** - Locked parameters displayed with 🔒 and status3. Startup config → set parameters3. Startup-Config → Parameter setzen

- **Unlock Functionality** - "🔓 Unlock" button for unlockable parameters

- **Lock Status Detection** - Automatic detection of read-only and inactive parameters4. Select first camera → set parameters4. Erste Kamera auswählen → Parameter setzen

- **Visual Lock Distinction** - Different icons and colors for different lock types

= Parameters set 3-4 times!= Parameter 3-4x gesetzt!

### Improved

- **Parameter Status Display** with color-coded indicators:

  - 🔒 (red) for READ-ONLY parameters

  - ⚠️ (orange) for INACTIVE parameters**AFTER this change:****NACH dieser Änderung:**

  - Unlock button only for unlockable parameters

- **Intelligent Unlock Strategies** - Automatic deactivation of auto modes1. Camera detection → only load1. Kamera-Erkennung → nur laden

- **Detailed Tooltips** for lock status with flag information

2. Load config → skipped (startup_complete=False)2. Config laden → wird übersprungen (startup_complete=False)

### New Unlock Strategies

- **exposure_absolute** ← disable exposure_auto3. Startup config → set parameters (only source at start)3. Startup-Config → Parameter setzen (einzige Quelle beim Start)

- **focus_absolute** ← disable focus_auto

- **white_balance_temperature** ← disable white_balance_temperature_auto4. startup_complete = True4. startup_complete = True

- **gain** ← disable gain_automatic

- **brightness/contrast/saturation** ← disable auto_exposure5. Select first camera → only display refresh5. Erste Kamera auswählen → nur Display-Refresh



## [0.0.0.12] - 2025-01-15= Parameters set 1 time!= Parameter 1x gesetzt!



### Added

- **Extended Camera Detection** - Check if cameras are preview-capable

- **Text Input Fields** for direct value input next to sliders### Logging Improvements### Logging-Verbesserungen

- **Parameter Tooltips** with English explanations for all camera parameters

- **Startup Configuration Menu** to select which cameras are configured at startup- "Startup complete - parameter changes will now be applied"- "Startup complete - parameter changes will now be applied"

- **Non-functional Camera Marking** with "[No Preview]" label

- "Skipping config load for /dev/videoX - startup not complete" (DEBUG)- "Skipping config load for /dev/videoX - startup not complete" (DEBUG)

### Improved

- **Camera Detection** now checks v4l2-ctl --list-formats for actual functionality- "Loaded saved config for /dev/videoX, refreshing display only"- "Loaded saved config for /dev/videoX, refreshing display only"

- **Parameter Controls** with combined slider + text input

- **User-Friendliness** through informative tooltips with parameter descriptions

- **Automatic Configuration** at application startup for defined cameras

## [0.0.0.19] - 2025-01-15## [0.0.0.19] - 2025-01-15

### Technical

- New helper methods: _is_capture_device(), _check_preview_capability()

- Parameter tooltip system with extensive description database

- StartupConfigWindow for graphical configuration management### Added### Hinzugefügt

- Extended camera availability checks

- JSON-based startup configuration storage- **CLI Arguments** - Command line support for various startup options- **CLI-Argumente** - Kommandozeilen-Unterstützung für verschiedene Start-Optionen



## [0.0.0.1] - 2025-10-15- **Minimized Start** - `--minimized` or `-m` starts application minimized- **Minimized Start** - `--minimized` oder `-m` startet Anwendung minimiert



### Added- **Debug Mode** - `--debug` enables debug logging- **Debug-Modus** - `--debug` aktiviert Debug-Logging

- **GUI Application** with tkinter for user-friendly operation

- **Automatic Camera Detection** of all available V4L2 devices- **Version Display** - `--version` shows version, also visible in window title- **Version-Anzeige** - `--version` zeigt Version an, auch im Fenstertitel sichtbar

- **Parameter Control** with intuitive sliders and input fields

  - Brightness- **Enhanced About Dialog** - Shows author (I3uLL3t), features and version- **Erweiterter About-Dialog** - Zeigt Autor (I3uLL3t), Features und Version

  - Contrast

  - Saturation- **Donation Button** - PayPal.me/i3ull3t link in About dialog and Help menu- **Spendenbutton** - PayPal.me/i3ull3t Link im About-Dialog und Help-Menü

  - Hue

  - White Balance- **Detailed Startup Logging** - Device path in all startup config logs- **Detailliertes Startup-Logging** - Device-Path in allen Startup-Config-Logs

  - Exposure (auto, absolute)

  - Gain

  - Sharpness

  - And all other available V4L2 parameters### Improved### Verbessert

- **Live Camera Preview** with OpenCV integration

  - Adjustable resolution- **Startup Configuration Logging** - Now shows device_path for each camera- **Startup-Configuration-Logging** - Zeigt jetzt device_path für jede Kamera

  - Real-time parameter updates

  - Thread-based performance- **Parameter Set Logging** - DEBUG level shows each parameter with device_path- **Parameter-Set-Logging** - DEBUG-Level zeigt jeden Parameter mit device_path

- **Configuration System** for persistent settings

  - JSON-based storage per camera- **About Dialog** - Full window instead of simple MessageBox- **About-Dialog** - Vollständiges Fenster statt einfacher MessageBox

  - Automatic loading on camera switch

  - Import/Export of configurations- **Version Management** - Central __version__ variable in main.py- **Versionsverwaltung** - Zentrale __version__ Variable in main.py

- **Backup System** for original parameters

  - Backup of original camera settings- **Logger Setup** - Now supports logging.Level integer parameter- **Logger-Setup** - Unterstützt jetzt logging.Level Integer-Parameter

  - One-click restore

  - Protection against accidental changes

- **Multi-Camera Support**

  - Dropdown selection between cameras### Technical### Technisch

  - Separate configurations per device

  - Hot-swap capable- argparse for CLI argument processing- argparse für CLI-Argument-Verarbeitung

- **Modular Architecture** for easy maintenance

  - Separate modules for Camera, GUI, Config, Utils- __version__ = "0.0.0.19" in main.py- __version__ = "0.0.0.19" in main.py

  - Clean interfaces between components

  - Extensible structure- start_minimized parameter for MainWindow- start_minimized Parameter für MainWindow



### Technical Features- version parameter passed to MainWindow- version Parameter durchgereicht an MainWindow

- **V4L2 Integration** via direct v4l2-ctl commands

- **Cross-Platform Compatibility** (development possible on Windows)- Detailed logging: device_path in all startup config messages- Detailliertes Logging: device_path in allen Startup-Config-Nachrichten

- **Logging System** with configurable log levels

- **Error Handling** with user-friendly error messages- webbrowser.open() for PayPal link- webbrowser.open() für PayPal-Link

- **Threading** for non-blocking GUI operations

- Centralized version display in window title- Zentralisierte Versions-Anzeige im Fenstertitel

### Build System

- **Automated Build Scripts** for Linux deployment

- **Development Tools** for easy development

- **PyInstaller Integration** for standalone executables### UI/UX Improvements### UI/UX Verbesserungen

- **Requirements Management** with pip

- **Desktop Integration** with .desktop files- **About Dialog with PayPal Button** - "☕ Support this project"- **About-Dialog mit PayPal-Button** - "☕ Support this project"



### Documentation- **Help Menu with Donate Option** - Direct access to donation link- **Help-Menü mit Donate-Option** - Direkter Zugang zu Spenden-Link

- **Comprehensive README** with installation and usage

- **Code Documentation** with docstrings- **Version Number in Title** - "CamLoader v0.0.0.19 - V4L2 Camera Controller"- **Versionsnummer im Titel** - "CamLoader v0.0.0.19 - V4L2 Camera Controller"

- **Examples** and troubleshooting guide

- **Architecture Overview** for developers- **Detailed Feature List** - All features listed in About dialog- **Detaillierte Feature-Liste** - Alle Features im About-Dialog aufgelistet



---- **Author Section** - "Developed by: I3uLL3t" with GitHub link- **Author-Sektion** - "Developed by: I3uLL3t" mit GitHub-Link



## Changelog Format



### Categories### CLI Usage### CLI-Nutzung

- **Added** for new features

- **Changed** for changes to existing functionality```bash```bash

- **Deprecated** for features that will be removed soon

- **Removed** for features removed in this version# Start normally# Normal starten

- **Fixed** for bug fixes

- **Security** for security updatespython src/main.pypython src/main.py



### Versioning

- **MAJOR** version for incompatible API changes

- **MINOR** version for new functionality (backwards compatible)# Start minimized# Minimiert starten

- **PATCH** version for bug fixes (backwards compatible)

python src/main.py --minimizedpython src/main.py --minimized



# With debug logging# Mit Debug-Logging

python src/main.py --debugpython src/main.py --debug



# Show version# Version anzeigen

python src/main.py --versionpython src/main.py --version

``````



### Logging Improvements### Logging-Verbesserungen

- "Processing startup config for device: /dev/videoX"- "Processing startup config for device: /dev/videoX"

- "Startup config disabled for /dev/videoX, skipping"- "Startup config disabled for /dev/videoX, skipping"

- "Applying startup config to /dev/videoX (CameraName)"- "Applying startup config to /dev/videoX (CameraName)"

- "Setting param=value on /dev/videoX" (DEBUG)- "Setting param=value on /dev/videoX" (DEBUG)

- "Successfully set param on /dev/videoX" (DEBUG)- "Successfully set param on /dev/videoX" (DEBUG)

- "Failed to set param on /dev/videoX" (WARNING)- "Failed to set param on /dev/videoX" (WARNING)



## [0.0.0.18] - 2025-01-15## [0.0.0.18] - 2025-01-15



### Fixed### Behoben

- **Slider-Text Synchronization** - Text input field now updates correctly when moving slider- **Slider-Text-Synchronisation** - Texteingabefeld aktualisiert sich jetzt korrekt beim Slider-Bewegen

- **Preview Camera Switch** - Preview automatically switches to new camera when active- **Preview-Kamera-Wechsel** - Preview wechselt automatisch zur neuen Kamera wenn aktiv

- **Detached Preview Camera Switch** - Detached preview also follows camera switch- **Detached-Preview-Kamera-Wechsel** - Auch abgetrenntes Preview folgt Kamerawechsel

- **Messagebox Foreground** - Messageboxes and dialogs now always appear in foreground- **Messagebox-Vordergrund** - Messageboxen und Dialoge erscheinen jetzt immer im Vordergrund



### Improved### Verbessert

- **Automatic Preview Restart** - Preview automatically restarts on camera switch if running- **Automatisches Preview-Restart** - Preview startet automatisch neu bei Kamerawechsel wenn es läuft

- **Dialog Focus Management** - lift() and focus_force() for all dialogs- **Dialog-Fokus-Management** - lift() und focus_force() für alle Dialoge

- **Text Entry Initialization** - _text_entry_vars initialized before slider creation- **Text-Entry-Initialisierung** - _text_entry_vars wird vor Slider-Erstellung initialisiert

- **Robust Camera Updates** - Synchronized updates for all preview windows- **Robuste Kamera-Updates** - Synchronisierte Updates für alle Preview-Fenster



### Technical### Technisch

- set_camera() saves preview status and restarts if it was active- set_camera() speichert Preview-Status und startet neu wenn aktiv war

- Detached preview window gets its own set_camera() method- Detached preview window erhält eigene set_camera() Methode

- Main window calls set_camera() for both preview types- Main window ruft set_camera() für beide Preview-Typen auf

- _text_entry_vars dictionary initialization before create_scale_control()- _text_entry_vars Dictionary-Initialisierung vor create_scale_control()

- lift() and focus_force() for root window before messagebox.showerror()- lift() und focus_force() für root window vor messagebox.showerror()

- Modal dialogs use lift() and focus_force() after grab_set()- Modal dialogs nutzen lift() und focus_force() nach grab_set()



### UI/UX Improvements### UI/UX Verbesserungen

- **Seamless Camera Switch** - Preview continues without interruption- **Nahtloser Kamerawechsel** - Preview läuft ohne Unterbrechung weiter

- **Better Dialog Visibility** - No more hidden dialogs- **Bessere Dialog-Sichtbarkeit** - Keine versteckten Dialoge mehr

- **Synchronized Inputs** - Slider and text field always in sync- **Synchronisierte Eingaben** - Slider und Textfeld immer in Sync

- **Consistent Preview Management** - Both preview modes behave identically- **Konsistente Preview-Verwaltung** - Beide Preview-Modi verhalten sich gleich



## [0.0.0.17] - 2025-01-15### Hinweis zu Startup-Parametern

- Startup-Konfiguration sendet NUR markierte Parameter (wie erwartet)

### Fixed- Code prüft include_var.get() vor Parameter-Übertragung

- **Critical Parameter Frame Error** - StringVar in parameter_widgets caused crashes on camera switch- Nur aktivierte Checkboxen werden in config["parameters"] gespeichert

- **Camera Switch Now Works** - Fully functional switching between cameras

- **Preview Problems Fixed** - Preview now works correctly after camera switch## [0.0.0.17] - 2025-01-15

- **Widget Cleanup Error** - Robust error handling when cleaning up parameter widgets

### Behoben

### Improved- **Kritischer Parameter-Frame-Fehler** - StringVar in parameter_widgets verursachte Crashes beim Kamerawechsel

- **Robust Widget Management** - Type checking before accessing widget_info dictionary- **Kamera-Wechsel funktioniert jetzt** - Vollständig funktionaler Wechsel zwischen Kameras

- **Safe Widget Destruction** - Try-catch around all destroy() calls- **Preview-Probleme behoben** - Preview funktioniert jetzt korrekt nach Kamerawechsel

- **Better Error Handling** - Warning instead of crash on unexpected widget type- **Widget-Cleanup-Fehler** - Robuste Fehlerbehandlung beim Aufräumen von Parameter-Widgets

- **Clean Data Structure** - No more StringVars directly in parameter_widgets

### Verbessert

### Technical- **Robuste Widget-Verwaltung** - Type-Checking vor Zugriff auf widget_info Dictionary

- Removed faulty StringVar storage in parameter_widgets (line 320)- **Sichere Widget-Zerstörung** - Try-Catch um alle destroy() Aufrufe

- isinstance() check for all widget_info entries- **Bessere Fehlerbehandlung** - Warnung statt Crash bei unerwartetem Widget-Typ

- Try-catch around frame.destroy() and widget.destroy() calls- **Saubere Datenstruktur** - Keine StringVars mehr direkt in parameter_widgets

- Logger warnings for unexpected widget types

- Separate storage of text_vars in _text_entry_vars dictionary### Technisch

- Entfernte fehlerhafte StringVar-Speicherung in parameter_widgets (Zeile 320)

### Root Cause- isinstance() Prüfung für alle widget_info Einträge

- `self.parameter_widgets[param.name + "_text_var"] = text_var` stored StringVar directly- Try-Catch um frame.destroy() und widget.destroy() Aufrufe

- `clear_parameters()` expected dictionary with 'frame' key for all entries- Logger-Warnungen für unerwartete Widget-Typen

- `widget_info['frame']` on StringVar caused "'StringVar' object is not subscriptable"- Separate Speicherung von text_vars in _text_entry_vars Dictionary

- Solution: Removed StringVar storage, only dictionaries in parameter_widgets

### Root Cause

## [0.0.0.16] - 2025-01-15- `self.parameter_widgets[param.name + "_text_var"] = text_var` speicherte StringVar direkt

- `clear_parameters()` erwartete Dictionary mit 'frame' Key für alle Einträge

### Fixed- `widget_info['frame']` auf StringVar verursachte "'StringVar' object is not subscriptable"

- **Critical Camera Selection Error** - StringVar error completely fixed with robust string conversion- Lösung: StringVar-Speicherung entfernt, nur Dictionaries in parameter_widgets

- **Improved Error Handling** - Detailed traceback for better error diagnosis

- **Config Loading Protection** - Additional type checks when loading camera configurations## [0.0.0.16] - 2025-01-15

- **Parse Error Handling** - Safe device path extraction with try-catch

### Behoben

### Improved- **Kritischer Kameraauswahl-Fehler** - StringVar-Fehler komplett behoben mit robuster String-Konvertierung

- **Robust String Conversion** - Explicit str() conversion for all camera selections- **Verbesserte Fehlerbehandlung** - Detaillierter Traceback für bessere Fehlerdiagnose

- **Type-Safe Config Loading** - isinstance() checks for all config accesses- **Config-Loading-Schutz** - Zusätzliche Typ-Prüfungen beim Laden von Kamera-Konfigurationen

- **Detailed Error Logging** - Full tracebacks for better debugging- **Parse-Error-Behandlung** - Sichere Device-Path-Extraktion mit Try-Catch

- **Safe Index Access** - IndexError and AttributeError are caught

### Verbessert

### Technical- **Robuste String-Konvertierung** - Explizite str() Konvertierung für alle Kamera-Auswahlen

- Explicit str() conversion in on_camera_selected()- **Type-Safe Config-Loading** - isinstance() Prüfungen für alle Config-Zugriffe

- Try-catch around device_path split() operations- **Detailliertes Error-Logging** - Vollständige Tracebacks für besseres Debugging

- isinstance() checks for config, parameters and param_data- **Sichere Index-Zugriffe** - IndexError und AttributeError werden abgefangen

- Full traceback.format_exc() in error logs

- Robust error handling in all critical paths### Technisch

- Explizite str() Konvertierung in on_camera_selected()

### Debugging Improvements- Try-Catch um device_path split() Operationen

- **Extended Stack Traces** - Complete error information in log- isinstance() Prüfungen für config, parameters und param_data

- **Parse Error Details** - Exact error source for device path parsing- Vollständige traceback.format_exc() in Error-Logs

- **Type Validation** - Explicit type checks before critical operations- Robuste Fehlerbehandlung in allen kritischen Pfaden



## [0.0.0.15] - 2025-01-15### Debugging-Verbesserungen

- **Erweiterte Stack-Traces** - Vollständige Fehlerinformationen im Log

### Fixed- **Parse-Error-Details** - Genaue Fehlerquelle bei Device-Path-Parsing

- **Slider-Text Synchronization** - Text input field now updates when moving slider- **Type-Validation** - Explizite Typ-Prüfungen vor kritischen Operationen

- **Camera Selection Error** - StringVar error in camera selection fixed

- **Startup Configuration Dialog** - Tkinter grab error when opening camera configuration fixed## [0.0.0.15] - 2025-01-15

- **Modal Dialog Problem** - Delayed grab_set() prevents "window not viewable" error

### Behoben

### Improved- **Slider-Text-Synchronisation** - Texteingabefeld aktualisiert sich jetzt beim Bewegen des Sliders

- **Bidirectional Parameter Synchronization** - Slider and text input fully synchronized- **Kameraauswahl-Fehler** - StringVar-Fehler bei der Kameraauswahl behoben

- **Extended Startup Parameter Configuration** - Better overview and input options- **Startup-Konfiguration-Dialog** - Tkinter Grab-Fehler beim Öffnen der Kamera-Konfiguration behoben

- **Parameter Display in Startup Dialog** - Shows current values and ranges for better orientation- **Modal-Dialog-Problem** - Verzögertes grab_set() verhindert "window not viewable" Fehler

- **Robust Camera Selection** - Better error handling for invalid selection formats

### Verbessert

### Technical- **Bidirektionale Parameter-Synchronisation** - Slider und Texteingabe sind vollständig synchronisiert

- Text entry variable synchronization between slider and input field- **Erweiterte Startup-Parameter-Konfiguration** - Bessere Übersicht und Eingabemöglichkeiten

- Delayed modal grab for startup configuration dialogs (100ms delay)- **Parameter-Anzeige in Startup-Dialog** - Zeigt aktuelle Werte und Bereiche für bessere Orientierung

- Improved StringVar handling in camera selection- **Robuste Kamera-Auswahl** - Bessere Fehlerbehandlung bei ungültigen Auswahlformaten

- Enhanced parameter controls in startup configuration with range display

- Automatic cleanup functions for text entry references### Technisch

- Text-Entry-Variablen-Synchronisation zwischen Slider und Eingabefeld

### UI/UX Improvements- Verzögertes Modal-Grab für Startup-Konfigurationsdialoge (100ms delay)

- **Startup Parameter Dialog** with current values and range information- Verbesserte StringVar-Behandlung in Kameraauswahl

- **Slider-Text Combination** - Both input methods stay synchronized- Enhanced Parameter-Kontrollen in Startup-Konfiguration mit Bereichsanzeige

- **Better Parameter Overview** in startup configuration- Automatische Cleanup-Funktionen für Text-Entry-Referenzen

- **Robust Dialog Handling** without grab errors

- **Precise Value Input** with slider and text field in startup configuration### UI/UX Verbesserungen

- **Startup-Parameter-Dialog** mit aktuellen Werten und Bereichsangaben

## [0.0.0.14] - 2025-01-15- **Slider-Text-Kombination** - Beide Eingabemethoden bleiben synchron

- **Bessere Parameter-Übersicht** in Startup-Konfiguration

### Added- **Robuste Dialog-Behandlung** ohne Grab-Fehler

- **Detachable Preview Window** - Preview can be moved to separate, movable window- **Präzise Werte-Eingabe** mit Slider und Textfeld in Startup-Konfiguration

- **New Layout Arrangement** - Parameters above preview for more space

- **"Detach Preview" Button** - Preview window can be detached from main application## [0.0.0.14] - 2025-01-15

- **Movable Preview Window** - Fully freely positionable and resizable

- **"Attach to Main" Function** - Preview window can be embedded back into main application### Hinzugefügt

- **Abtrennbares Preview-Fenster** - Preview kann in separates, verschiebbares Fenster ausgelagert werden

### Improved- **Neue Layout-Anordnung** - Parameter oberhalb der Vorschau für mehr Platz

- **More Space for Parameters** - Vertical arrangement gives parameters more room- **"Detach Preview" Button** - Preview-Fenster kann von der Hauptanwendung getrennt werden

- **Flexible Window Management** - Preview can be displayed as needed- **Bewegliches Preview-Fenster** - Vollständig frei positionierbar und größenveränderbar

- **Better Workspace Usage** - Main window can be used without preview- **"Attach to Main" Funktion** - Preview-Fenster kann wieder in Hauptanwendung eingebettet werden

- **Dynamic Size Adjustment** - Preview window adapts to content

### Verbessert

### Technical- **Mehr Platz für Parameter** - Vertikale Anordnung gibt Parametern mehr Raum

- DetachedPreviewWindow class for standalone preview window- **Flexiblere Fenster-Verwaltung** - Preview kann je nach Bedarf angezeigt werden

- Extended PreviewFrame with detach/attach functionality- **Bessere Arbeitsbereich-Nutzung** - Hauptfenster kann ohne Preview genutzt werden

- Revised MainWindow layout structure (vertical instead of horizontal)- **Dynamische Größenanpassung** - Preview-Fenster passt sich an Inhalt an

- Intelligent preview state transfer between windows

- Automatic window management and cleanup functions### Technisch

- DetachedPreviewWindow-Klasse für eigenständiges Preview-Fenster

### UI/UX Improvements- Erweiterte PreviewFrame mit Detach/Attach-Funktionalität

- Vertical main layout for better parameter overview- Überarbeitete MainWindow-Layout-Struktur (vertikal statt horizontal)

- "Detach Preview" button in preview control area- Intelligente Preview-State-Übertragung zwischen Fenstern

- Standalone preview windows with start/stop/attach controls- Automatische Fenster-Management und Cleanup-Funktionen

- Adjustable window size and free positioning

- Automatic preview state management between windows### UI/UX Verbesserungen

- Vertikales Haupt-Layout für bessere Parameter-Übersicht

## [0.0.0.13] - 2025-01-15- "Detach Preview" Button in Preview-Kontrollbereich

- Eigenständige Preview-Fenster mit Start/Stop/Attach-Kontrollen

### Added- Anpassbare Fenstergröße und freie Positionierung

- **Parameter Lock Visualization** - Locked parameters displayed with 🔒 and status- Automatisches Preview-State-Management zwischen Fenstern

- **Unlock Functionality** - "🔓 Unlock" button for unlockable parameters

- **Lock Status Detection** - Automatic detection of read-only and inactive parameters## [0.0.0.13] - 2025-01-15

- **Visual Lock Distinction** - Different icons and colors for different lock types

### Hinzugefügt

### Improved- **Parameter-Lock-Visualisierung** - Gesperrte Parameter werden mit 🔒 und Status angezeigt

- **Parameter Status Display** with color-coded indicators:- **Unlock-Funktionalität** - "🔓 Unlock" Button für entsperrbare Parameter

  - 🔒 (red) for READ-ONLY parameters- **Lock-Status-Erkennung** - Automatische Erkennung von read-only und inactive Parametern

  - ⚠️ (orange) for INACTIVE parameters- **Visuelle Lock-Unterscheidung** - Verschiedene Icons und Farben für verschiedene Lock-Typen

  - Unlock button only for unlockable parameters

- **Intelligent Unlock Strategies** - Automatic deactivation of auto modes### Verbessert

- **Detailed Tooltips** for lock status with flag information- **Parameter-Status-Anzeige** mit farbcodierten Indikatoren:

- **Parameter Frame Layout** for better overview of locked parameters  - 🔒 (rot) für READ-ONLY Parameter

  - ⚠️ (orange) für INACTIVE Parameter

### Technical  - Unlock-Button nur für entsperrbare Parameter

- Extended V4L2Parameter class with is_readonly, is_inactive, flags properties- **Intelligente Unlock-Strategien** - Automatisches Deaktivieren von Auto-Modi

- Flag parsing in _parse_control_line for v4l2-ctl output- **Detaillierte Tooltips** für Lock-Status mit Flag-Informationen

- try_unlock_parameter() method with auto parameter deactivation- **Parameter-Frame-Layout** für bessere Übersichtlichkeit bei gesperrten Parametern

- get_locking_parameters() for parameter dependency mapping

- Visual lock status framework with icons and color coding### Technisch

- Erweiterte V4L2Parameter-Klasse mit is_readonly, is_inactive, flags Properties

### New Unlock Strategies- Flag-Parsing in _parse_control_line für v4l2-ctl Output

- **exposure_absolute** ← disable exposure_auto- try_unlock_parameter() Methode mit Auto-Parameter-Deaktivierung

- **focus_absolute** ← disable focus_auto- get_locking_parameters() für Parameter-Abhängigkeits-Mapping

- **white_balance_temperature** ← disable white_balance_temperature_auto- Visual Lock-Status-Framework mit Icons und Farbcodierung

- **gain** ← disable gain_automatic

- **brightness/contrast/saturation** ← disable auto_exposure### Neue Unlock-Strategien

- **exposure_absolute** ← exposure_auto deaktivieren

### UI/UX Improvements- **focus_absolute** ← focus_auto deaktivieren  

- Disabled controls for locked parameters- **white_balance_temperature** ← white_balance_temperature_auto deaktivieren

- Unlock help with current values of locking parameters- **gain** ← gain_automatic deaktivieren

- Success/error messages for unlock attempts- **brightness/contrast/saturation** ← auto_exposure deaktivieren

- Automatic parameter refresh after successful unlock

### UI/UX Verbesserungen

## [0.0.0.12] - 2025-01-15- Deaktivierte Kontrollen für gesperrte Parameter

- Unlock-Hilfe mit aktuellen Werten der sperrenden Parameter

### Added- Erfolgs-/Fehlermeldungen für Unlock-Versuche

- **Extended Camera Detection** - Check if cameras are preview-capable- Automatische Parameter-Refresh nach erfolgreichem Unlock

- **Text Input Fields** for direct value input next to sliders

- **Parameter Tooltips** with English explanations for all camera parameters## [0.0.0.12] - 2025-01-15

- **Startup Configuration Menu** to select which cameras are configured at startup

- **Non-functional Camera Marking** with "[No Preview]" label### Hinzugefügt

- **Erweiterte Kamera-Erkennung** - Überprüfung ob Kameras Preview-fähig sind

### Improved- **Text-Eingabefelder** für direkte Werteingabe neben Schiebereglern

- **Camera Detection** now checks v4l2-ctl --list-formats for actual functionality- **Parameter-Tooltips** mit englischen Erklärungen für alle Kamera-Parameter

- **Parameter Controls** with combined slider + text input- **Startup-Konfiguration-Menü** zur Auswahl welche Kameras beim Start konfiguriert werden

- **User-Friendliness** through informative tooltips with parameter descriptions- **Nicht-funktionale Kamera-Kennzeichnung** mit "[No Preview]" Markierung

- **Automatic Configuration** at application startup for defined cameras

### Verbessert

### Technical- **Kamera-Erkennung** prüft jetzt v4l2-ctl --list-formats für tatsächliche Funktionalität

- New helper methods: _is_capture_device(), _check_preview_capability()- **Parameter-Kontrollen** mit kombinierten Schieberegler + Texteingabe

- Parameter tooltip system with extensive description database- **Benutzerfreundlichkeit** durch informative Tooltips mit Parameterbeschreibungen

- StartupConfigWindow for graphical configuration management- **Automatische Konfiguration** beim Anwendungsstart für definierte Kameras

- Extended camera availability checks

- JSON-based startup configuration storage### Technisch

- Neue Hilfsmethoden: _is_capture_device(), _check_preview_capability()

### New Features- Parameter-Tooltip-System mit umfangreicher Beschreibungsdatenbank

- **Startup Configuration Dialog** - Complete GUI for camera startup settings- StartupConfigWindow für grafische Konfigurationsverwaltung

- **Parameter Range Validation** - Automatic value range checking in text inputs- Erweiterte Kamera-Verfügbarkeitsprüfungen

- **Camera Capability Detection** - Distinction between existing and functional cameras- JSON-basierte Startup-Konfigurationsspeicherung

- **Enhanced Tooltips** - Over 30 detailed parameter explanations in English

### Neue Features

---- **Startup Configuration Dialog** - Vollständige GUI für Kamera-Startup-Einstellungen

- **Parameter Range Validation** - Automatische Wertebereichsprüfung in Texteingaben

## Changelog Format- **Camera Capability Detection** - Unterscheidung zwischen existierenden und funktionalen Kameras

- **Enhanced Tooltips** - Über 30 detaillierte Parameter-Erklärungen in englischer Sprache

### Categories

- **Added** for new features## [0.0.0.11] - 2025-01-15

- **Changed** for changes to existing functionality

- **Deprecated** for features that will be removed soon### Behoben

- **Removed** for features removed in this version- **Python-Version-Problem** - Build verwendete immer noch Python 3.11 statt 3.8

- **Fixed** for bug fixes- **GLIBC 2.38 Abhängigkeit** durch Downgrade auf Python 3.8 eliminiert

- **Security** for security updates- **Explizite Python-Interpreter-Verwendung** in allen Build-Schritten

- **PyInstaller Python-Version-Verifikation** hinzugefügt

### Versioning

- **MAJOR** version for incompatible API changes### Geändert

- **MINOR** version for new functionality (backwards compatible)- **Python-Version** von 3.9 auf 3.8 reduziert für maximale Kompatibilität

- **PATCH** version for bug fixes (backwards compatible)- **Konsistente Python-Verwendung** (python statt python3) im gesamten Workflow

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