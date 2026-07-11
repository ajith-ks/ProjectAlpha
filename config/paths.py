"""
Project paths.

All project directories are defined here.
"""

from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

LOG_DIR = PROJECT_ROOT / "logs"
REPORT_DIR = PROJECT_ROOT / "reports"
CHART_DIR = PROJECT_ROOT / "charts"

# Create directories automatically
for directory in (
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    LOG_DIR,
    REPORT_DIR,
    CHART_DIR,
):
    directory.mkdir(parents=True, exist_ok=True)