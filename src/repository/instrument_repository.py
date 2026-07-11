"""
Instrument Repository

Loads instrument metadata from local JSON files.
"""

import json
from pathlib import Path

from src.models import Instrument


class InstrumentRepository:
    """Repository for loading instrument metadata."""

    def __init__(self, metadata_file: Path) -> None:
        self.metadata_file = metadata_file

    def load(self) -> list[Instrument]:
        """Load all instruments."""

        with self.metadata_file.open(
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

        return [
            Instrument(**item)
            for item in data
        ]

    def get(self, name: str) -> Instrument:
        """Return instrument by name."""

        instruments = self.load()

        for instrument in instruments:
            if instrument.name == name:
                return instrument

        raise ValueError(
            f"Unknown instrument: {name}"
        )