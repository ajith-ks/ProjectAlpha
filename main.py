from pathlib import Path

from src.repository import InstrumentRepository

repository = InstrumentRepository(
    Path("resources/instruments/dukascopy.json")
)

gold = repository.get("XAU/USD")

print(gold)