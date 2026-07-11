"""
Dukascopy Historical Data Downloader
"""

import httpx

from src.utils.logger import get_logger


class DukascopyDownloader:
    """Downloader for Dukascopy historical data."""

    BASE_URL = "https://freeserv.dukascopy.com/2.0/"

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)

        self.client = httpx.Client(
            timeout=30.0,
            follow_redirects=True,
        )

        self.logger.info("Downloader initialized.")

    def close(self) -> None:
        """Close the HTTP client."""
        self.client.close()
        self.logger.info("Downloader closed.")