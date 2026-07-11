"""
Dukascopy URL Builder
"""

from datetime import date

from src.models import Instrument


class DukascopyURLBuilder:
    """Builds Dukascopy historical data URLs."""

    BASE_URL = "https://datafeed.dukascopy.com/datafeed"

    def build_minute_url(
        self,
        instrument: Instrument,
        target_date: date,
    ) -> str:

        year = target_date.year

        month = f"{target_date.month - 1:02d}"

        day = f"{target_date.day:02d}"

        return (
            f"{self.BASE_URL}/"
            f"{instrument.historical_filename}/"
            f"{year}/"
            f"{month}/"
            f"{day}/"
            "BID_candles_min_1.bi5"
        )