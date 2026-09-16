"""Misc system utilities."""
from datetime import datetime


def get_time() -> str:
    now = datetime.now().strftime("%I:%M %p")
    return f"It's currently {now}."
