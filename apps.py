"""Application launching, Windows-focused."""
import subprocess

# Map friendly names -> how to launch them on Windows.
# "start" uses the Windows shell, which resolves normal installed apps by
# their App Paths registry entries (works for Chrome, Edge, Notepad, etc.
# without needing the full exe path).
KNOWN_APPS = {
    "chrome": "chrome",
    "google chrome": "chrome",
    "edge": "msedge",
    "notepad": "notepad",
    "vscode": "code",
    "vs code": "code",
    "visual studio code": "code",
    "explorer": "explorer",
    "file explorer": "explorer",
    "calculator": "calc",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "spotify": "spotify",
}


def open_application(application: str) -> str:
    key = application.strip().lower()
    exe = KNOWN_APPS.get(key, key)  # fall back to trying the raw name
    try:
        subprocess.Popen(f'start "" "{exe}"', shell=True)
        return f"Opened {application}."
    except Exception as e:
        return f"Couldn't open {application}: {e}"
