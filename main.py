from src.data.dukascopy_downloader import DukascopyDownloader

downloader = DukascopyDownloader()

print()
print(f"Raw Data Directory : {downloader.get_output_directory()}")