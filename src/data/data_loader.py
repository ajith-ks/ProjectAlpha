"""
Historical Data Loader

Loads market data from the configured data directory.
"""

from pathlib import Path

import pandas as pd

from config.settings import DATA_DIRECTORY


class DataLoader:
    """
    Loads historical market data.
    """

    def __init__(self) -> None:
        self.data_directory: Path = DATA_DIRECTORY

    def list_available_files(self) -> list[Path]:
        """
        Return all CSV files in the raw data directory.
        """
        return sorted(self.data_directory.glob("*.csv"))

    def file_exists(self, filename: str) -> bool:
        """
        Check whether a file exists.
        """
        return (self.data_directory / filename).exists()