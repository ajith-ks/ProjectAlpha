"""
Instrument Service

Business logic for instrument metadata.
"""

from src.models import Instrument
from src.repository import InstrumentRepository


class InstrumentService:
    """Service for instrument operations."""

    def __init__(self, repository: InstrumentRepository) -> None:
        self.repository = repository

    def get(self, name: str) -> Instrument:
        """Return an instrument by name."""
        return self.repository.get(name)

    def list(self) -> list[Instrument]:
        """Return all available instruments."""
        return self.repository.load()