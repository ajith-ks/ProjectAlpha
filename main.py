from src.data.data_loader import DataLoader
from src.utils.logger import get_logger

logger = get_logger("ProjectAlpha")

loader = DataLoader()

logger.info("Application started")

print()
print("Available data files:")

files = loader.list_available_files()

if not files:
    print("  No historical data found.")
else:
    for file in files:
        print(f"  - {file.name}")