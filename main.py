from pathlib import Path

from src.repository import InstrumentRepository
from src.services import InstrumentService

repository = InstrumentRepository(
    Path("resources/instruments/dukascopy.json")
)

service = InstrumentService(repository)

gold = service.get("XAU/USD")

print(gold)