"""
Timezone utility functions.

All internal timestamps are UTC.
Display timestamps are converted to IST.
"""

from datetime import datetime, timezone

from config.settings import DISPLAY_ZONE


def utc_now() -> datetime:
    """
    Return the current UTC time.
    """
    return datetime.now(timezone.utc)


def utc_to_ist(dt: datetime) -> datetime:
    """
    Convert a UTC datetime to IST.

    Args:
        dt: UTC datetime

    Returns:
        Datetime converted to IST
    """
    return dt.astimezone(DISPLAY_ZONE)


def format_datetime(dt: datetime) -> str:
    """
    Format datetime for display.

    Example:
    11-Jul-2026 14:30 IST
    """
    return dt.strftime("%d-%b-%Y %H:%M %Z")