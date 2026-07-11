"""
Dukascopy Historical Data Downloader

Downloads historical XAUUSD data from Dukascopy.
"""

from pathlib import Path

from config.paths import RAW_DATA_DIR
from src.utils.logger import get_logger


class DukascopyDownloader:
    """
    Downloader for Dukascopy historical data.
    """

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)
        self.output_directory: Path = RAW_DATA_DIR

        self.logger.info("Dukascopy downloader initialized.")

    def get_output_directory(self) -> Path:
        """
        Return the raw data directory.
        """
        return self.output_directory