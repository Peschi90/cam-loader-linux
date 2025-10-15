# Release-System Anleitung

## Übersicht

Das CamLoader-Projekt verfügt über ein vollautomatisches Release-System, das bei jedem Git-Tag eine neue Version erstellt. Das System:

1. **Extrahiert automatisch Changelog-Einträge** aus `CHANGELOG.md`
2. **Erstellt Linux-Executables** mit PyInstaller
3. **Baut Source- und Wheel-Distributionen**
4. **Veröffentlicht alles auf GitHub Releases**

## 🚀 Schnellstart: Neues Release erstellen

### 1. CHANGELOG.md aktualisieren

Fügen Sie Ihre Änderungen in die `CHANGELOG.md` ein:

```markdown
## [1.1.0] - 2025-10-16

### Hinzugefügt
- Neue Feature XYZ
- Verbesserte Performance

### Behoben
- Bug in der Kamera-Erkennung
```

### 2. Version in setup.py aktualisieren

```python
setup(
    name="camloader",
    version="1.1.0",  # <- Hier aktualisieren
    # ...
)
```

### 3. Git Tag erstellen und pushen

```bash
# Tag erstellen
git tag v1.1.0

# Tag zu GitHub pushen (startet automatisch das Release)
git push origin v1.1.0
```

Das war's! Der Rest passiert automatisch.

## 📦 Was wird erstellt

Jedes Release enthält:

1. **`camloader-vX.X.X-linux-x86_64.tar.gz`** - Standalone Linux-Executable
2. **`camloader-vX.X.X-linux-x86_64.zip`** - Dasselbe als ZIP
3. **`camloader-vX.X.X-source.tar.gz`** - Source Code Distribution
4. **`camloader-vX.X.X-py3-none-any.whl`** - Python Wheel

## 🔍 Release-Pakete im Detail

### Linux Executable Paket

Das `.tar.gz`/`.zip` Paket enthält:

```
camloader-v1.0.0-linux-x86_64/
├── camloader              # Standalone executable
├── camloader.sh           # Wrapper script with dependency checks
├── install.sh             # System installation script
├── camloader.desktop      # Desktop entry file
├── README.md              # Documentation
├── LICENSE                # License file
├── CHANGELOG.md           # Changelog
└── README_PACKAGE.txt     # Package-specific instructions
```

#### Verwendung:

```bash
# Entpacken
tar -xzf camloader-v1.0.0-linux-x86_64.tar.gz
cd camloader-v1.0.0-linux-x86_64

# Direkt ausführen
./camloader.sh

# Oder system-weit installieren
sudo ./install.sh
```

## 🛠️ Lokaler Test des Release-Systems

Vor dem eigentlichen Release können Sie alles lokal testen:

```bash
# Release-Test ausführen
chmod +x scripts/test-release.sh
./scripts/test-release.sh 1.1.0

# Oder mit dem Development-Script
./scripts/dev.sh test
```

## 📝 CHANGELOG.md Format

### Struktur

```markdown
# Changelog

## [Unreleased]
### Geplant
- Feature für nächste Version

## [1.1.0] - 2025-10-16
### Hinzugefügt
- Neue Features

### Geändert
- Modifikationen

### Behoben
- Bugfixes

## [1.0.0] - 2025-10-15
### Hinzugefügt
- Initial release
```

### Kategorien

- **Hinzugefügt** - Neue Features
- **Geändert** - Änderungen an bestehender Funktionalität
- **Veraltet** - Features die bald entfernt werden
- **Entfernt** - Entfernte Features
- **Behoben** - Bugfixes
- **Sicherheit** - Sicherheitsupdates

## 🔧 GitHub Actions Workflow

### Datei: `.github/workflows/release.yml`

Das Workflow besteht aus drei Jobs:

1. **`create-release`** - Erstellt das GitHub Release
2. **`build-linux-executable`** - Baut das Linux Executable
3. **`build-source-package`** - Erstellt Source/Wheel Distributionen

### Trigger

```yaml
on:
  push:
    tags:
      - 'v*'  # Alle Tags die mit 'v' beginnen
```

### Permissions

```yaml
permissions:
  contents: write  # Für Release-Erstellung
```

## ⚙️ PyInstaller Konfiguration

### Datei: `camloader.spec`

Die Konfiguration erstellt ein standalone Executable mit:

- Alle Python-Dependencies eingebettet
- GUI-optimiert (kein Konsolen-Fenster)
- UPX-Komprimierung für kleinere Dateigröße
- Automatisches Einbinden der `data/` Verzeichnisse

### Hidden Imports

Wichtige Module die explizit eingebunden werden:

```python
hiddenimports=[
    'tkinter', 'tkinter.ttk',
    'PIL', 'PIL.Image', 'PIL.ImageTk',
    'cv2', 'psutil',
    'camera', 'gui', 'config', 'utils'
]
```

## 🎯 Versionierung

Wir folgen [Semantic Versioning](https://semver.org/):

- **MAJOR** (X.0.0) - Inkompatible API-Änderungen
- **MINOR** (0.X.0) - Neue Features (rückwärtskompatibel)
- **PATCH** (0.0.X) - Bugfixes (rückwärtskompatibel)

### Pre-Release Versionen

Tags mit Bindestrich werden als Pre-Release markiert:

```bash
git tag v1.1.0-beta1    # Pre-release
git tag v1.1.0-rc1      # Release candidate
git tag v1.1.0          # Stable release
```

## 🚨 Fehlerbehebung

### Release schlägt fehl

1. **Prüfen Sie die GitHub Actions Logs**
2. **Häufige Probleme:**
   - CHANGELOG.md Format ungültig
   - Version in setup.py vergessen zu aktualisieren
   - Build-Dependencies fehlen

### Changelog wird nicht extrahiert

Prüfen Sie das Format in `CHANGELOG.md`:

```bash
# Lokal testen
python -c "
import re
with open('CHANGELOG.md', 'r') as f:
    content = f.read()
pattern = r'##\s*\[1\.0\.0\].*?\n(.*?)(?=\n##|\n#|\Z)'
match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
print(match.group(1) if match else 'Not found')
"
```

### PyInstaller Build schlägt fehl

1. **Dependencies prüfen:**
   ```bash
   pip install -r requirements.txt
   pip install pyinstaller
   ```

2. **Lokal testen:**
   ```bash
   pyinstaller camloader.spec --clean
   ./dist/camloader --help
   ```

## 📚 Erweiterte Nutzung

### Manueller Release (ohne GitHub Actions)

```bash
# 1. Build Executable
pyinstaller camloader.spec --clean

# 2. Source Distribution
python -m build --sdist

# 3. Wheel
python -m build --wheel

# 4. Package erstellen
./scripts/build.sh
```

### Custom Release Notes

Wenn Sie spezielle Release Notes benötigen, können Sie diese nach dem automatischen Release manuell in GitHub editieren.

### Multi-Platform Builds

Für Windows/macOS Builds erweitern Sie die GitHub Actions um entsprechende Runner:

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
```

## ✅ Checkliste für Releases

- [ ] CHANGELOG.md aktualisiert
- [ ] Version in setup.py erhöht
- [ ] Lokaler Test erfolgreich: `./scripts/test-release.sh`
- [ ] Alle Tests bestehen: `./scripts/dev.sh test`
- [ ] Git Tag erstellt: `git tag vX.X.X`
- [ ] Tag gepusht: `git push origin vX.X.X`
- [ ] GitHub Actions erfolgreich
- [ ] Release auf GitHub veröffentlicht

---

Das Release-System ist vollautomatisch und robust. Bei Fragen prüfen Sie die GitHub Actions Logs oder testen Sie lokal mit den bereitgestellten Scripts.