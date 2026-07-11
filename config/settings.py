"""
Project Alpha Configuration

All configurable settings are maintained here.
Do not hardcode configuration values elsewhere.
"""

from zoneinfo import ZoneInfo
from config.paths import RAW_DATA_DIR, LOG_DIR
# ==========================================================
# Project Information
# ==========================================================

PROJECT_NAME = "Project Alpha"

VERSION = "0.1.0"

# ==========================================================
# Time Zones
# ==========================================================

UTC_ZONE = ZoneInfo("UTC")

DISPLAY_ZONE = ZoneInfo("Asia/Kolkata")

DISPLAY_ZONE_NAME = "IST"

# ==========================================================
# Trading Instrument
# ==========================================================

SYMBOL = "XAUUSD"

# ==========================================================
# Timeframes
# ==========================================================

EXECUTION_TIMEFRAME = "M5"

TREND_TIMEFRAME = "H4"

CONFIRMATION_TIMEFRAME = "H1"

# ==========================================================
# Risk Management
# ==========================================================

RISK_PER_TRADE = 0.01

RISK_REWARD = 2.0

# ==========================================================
# Data
# ==========================================================

DATA_SOURCE = "Dukascopy"

DATA_DIRECTORY = RAW_DATA_DIR


# ==========================================================
# Logging
# ==========================================================

LOG_DIRECTORY = LOG_DIR