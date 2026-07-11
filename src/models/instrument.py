"""
Instrument model.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Instrument:
    """
    Represents a trading instrument.
    """

    name: str
    historical_filename: str
    pip_value: float
    point_value: float