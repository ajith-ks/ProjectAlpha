from datetime import date
from pathlib import Path

from src.downloader import DukascopyURLBuilder
from src.repository import InstrumentRepository
from src.services import InstrumentService

repository = InstrumentRepository(
    Path("resources/instruments/dukascopy.json")
)

service = InstrumentService(repository)

gold = service.get("XAU/USD")

builder = DukascopyURLBuilder()

url = builder.build_minute_url(
    gold,
    date(2024, 1, 15),
)

print(url)