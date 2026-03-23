# SpeedShift

SpeedShift is a Python speed converter with:
- CLI version (Linux terminal)
- Tkinter desktop GUI
- Kivy Android app source (phone + tablet ready)

## 1) CLI Version

Run:

```bash
python3 speedshift.py
```

## 2) Desktop GUI Version (Tkinter)

Run:

```bash
python3 speedshift_gui.py
```

### GUI features
- Light / Dark mode toggle
- Supports km/h, mph, m/s, knots, ft/s, cm/s, Mach (approx)
- Clear and Exit buttons

## 3) Android Version (Kivy + Buildozer)

Android source files are in `android_app/`.

### What this supports
- Phones (e.g., Samsung Galaxy S24)
- Tablets (e.g., Samsung Galaxy Tab S10 FE+)
- Single UI that scales with Android screen size

### A) Local desktop preview in VS Code

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r android_app/requirements.txt
python3 android_app/main.py
```

### B) Build an Android APK on Kali Linux

Install dependencies (one-time):

```bash
sudo apt update
sudo apt install -y python3-pip git zip unzip openjdk-17-jdk
pip install buildozer cython
```

Then build:

```bash
cd android_app
buildozer -v android debug
```

The APK is generated under:

```text
android_app/bin/
```

### C) Install on your Samsung devices

1. Enable **Developer options** on device.
2. Enable **USB debugging**.
3. Connect via USB and trust your computer.
4. Install with adb:

```bash
adb devices
adb install -r android_app/bin/*.apk
```

## Shared conversion core

`speedshift_core.py` contains conversion logic used by CLI, Tkinter GUI, and Android app.

## Version

Current project version: **1.3**
