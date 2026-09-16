"""File and folder operations."""
import os
from pathlib import Path


def create_folder(path: str) -> str:
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        return f"Created folder {path}."
    except Exception as e:
        return f"Couldn't create that folder: {e}"


def delete_file(path: str, confirmed: bool) -> str:
    """
    Deletion always requires explicit confirmation. main.py asks the user
    "yes/no" out loud/typed BEFORE calling this with confirmed=True.
    """
    if not confirmed:
        return "Deletion cancelled."
    try:
        p = Path(path)
        if p.is_dir():
            os.rmdir(p)
        else:
            p.unlink()
        return f"Deleted {path}."
    except Exception as e:
        return f"Couldn't delete that: {e}"


def take_screenshot() -> str:
    try:
        import pyautogui
        from datetime import datetime
        from config import DATA_DIR

        filename = DATA_DIR / f"screenshot_{datetime.now():%Y%m%d_%H%M%S}.png"
        pyautogui.screenshot(str(filename))
        return f"Screenshot saved to {filename}."
    except Exception as e:
        return f"Couldn't take a screenshot: {e}"
