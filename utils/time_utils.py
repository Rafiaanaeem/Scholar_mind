from datetime import datetime
from zoneinfo import ZoneInfo

PAKISTAN_TZ = ZoneInfo("Asia/Karachi")


def utc_to_local(timestamp: str) -> str:
    """Convert a SQLite UTC timestamp to Pakistan local time."""

    utc_time = datetime.strptime(
        timestamp,
        "%Y-%m-%d %H:%M:%S"
    ).replace(tzinfo=ZoneInfo("UTC"))

    local_time = utc_time.astimezone(PAKISTAN_TZ)

    return local_time.strftime("%Y-%m-%d %H:%M:%S")