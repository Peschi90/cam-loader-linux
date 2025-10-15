# CamLoader Troubleshooting Guide

## Ausführbare Datei startet nicht auf Debian/Ubuntu

### Häufige Probleme und Lösungen

#### 1. Berechtigungen überprüfen
```bash
# Ausführbare Berechtigung setzen
chmod +x camloader-linux-x86_64

# Überprüfen der Berechtigungen
ls -la camloader-linux-x86_64
```

#### 2. Fehlende System-Bibliotheken
```bash
# Auf Debian/Ubuntu erforderliche Pakete installieren:
sudo apt update
sudo apt install -y python3-tk python3-pil python3-pil.imagetk v4l-utils

# Für ältere Systeme zusätzlich:
sudo apt install -y libgtk-3-0 libgdk-pixbuf2.0-0 libfontconfig1 libxrender1 libxinerama1 libxi6 libxrandr2 libxcursor1 libxcomposite1 libxdamage1 libxfixes3 libxss1 libxtst6 libasound2

# OpenCV-Abhängigkeiten:
sudo apt install -y libopencv-dev python3-opencv
```

#### 3. Debug-Informationen sammeln

**Option A: Debug-Wrapper verwenden**
```bash
# Debug-Wrapper herunterladen und verwenden
wget https://github.com/Peschi90/cam-loader-linux/releases/latest/download/camloader-debug.sh
chmod +x camloader-debug.sh
./camloader-debug.sh
```

**Option B: Manuell debuggen**
```bash
# Dateityp überprüfen
file camloader-linux-x86_64

# Bibliotheks-Abhängigkeiten prüfen
ldd camloader-linux-x86_64

# Mit Fehlerausgabe starten
./camloader-linux-x86_64 2>&1 | tee camloader-error.log
```

#### 4. Systemkompatibilität

**Mindestanforderungen:**
- Linux x86_64 (64-bit)
- GLIBC >= 2.17 (Ubuntu 14.04+, Debian 8+)
- X11 (GUI-Umgebung)
- Python 3.7+ kompatible Bibliotheken

**Kompatibilitätscheck:**
```bash
# GLIBC-Version prüfen
ldd --version

# X11 verfügbar?
echo $DISPLAY
xdpyinfo 2>/dev/null && echo "X11 OK" || echo "X11 Problem"

# V4L2-Geräte verfügbar?
ls /dev/video* 2>/dev/null || echo "Keine Kameras gefunden"
```

#### 5. Alternative: Python-Umgebung

Falls die ausführbare Datei nicht funktioniert, können Sie das Programm direkt mit Python ausführen:

```bash
# Repository klonen
git clone https://github.com/Peschi90/cam-loader-linux.git
cd cam-loader-linux

# Abhängigkeiten installieren
pip3 install -r requirements.txt

# Programm starten
python3 src/main.py
```

### Fehlermeldungen und deren Bedeutung

| Fehlermeldung | Ursache | Lösung |
|---------------|---------|---------|
| `./camloader-linux-x86_64: No such file or directory` | 32-bit System oder fehlende Bibliotheken | GLIBC und Abhängigkeiten installieren |
| `ImportError: No module named '_tkinter'` | Tkinter nicht verfügbar | `sudo apt install python3-tk` |
| `cv2.error: OpenCV(4.x)` | OpenCV-Problem | `sudo apt install python3-opencv` |
| `Permission denied` | Keine Ausführberechtigung | `chmod +x camloader-linux-x86_64` |
| Schwarzes Fenster ohne Inhalt | GUI-Bibliotheken fehlen | Libgtk und X11-Pakete installieren |

### Support

Bei weiterhin bestehenden Problemen:

1. Debug-Log erstellen:
   ```bash
   ./camloader-debug.sh > debug-output.txt 2>&1
   ```

2. Issue auf GitHub erstellen mit:
   - Debian/Ubuntu Version (`lsb_release -a`)
   - Architektur (`uname -m`)
   - Debug-Log Inhalt
   - Fehlermeldung

3. Link: https://github.com/Peschi90/cam-loader-linux/issues