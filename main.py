import json
from pathlib import Path

from src.models import Instrument

metadata = Path("resources/instruments/dukascopy.json")

with metadata.open(encoding="utf-8") as file:
    instruments = json.load(file)

gold = Instrument(**instruments[0])

print(gold)