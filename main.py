from src.utils.logger import get_logger
from src.utils.timezone import (
    utc_now,
    utc_to_ist,
    format_datetime,
)

logger = get_logger("ProjectAlpha")

utc_time = utc_now()
ist_time = utc_to_ist(utc_time)

logger.info("Application started")

print()
print(f"UTC : {format_datetime(utc_time)}")
print(f"IST : {format_datetime(ist_time)}")