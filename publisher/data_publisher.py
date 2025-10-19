import requests
import logging


SPRING_BASE_URL = "http://43.203.153.18/process/api/ingest"

logger = logging.getLogger(__name__)


def send_minute_data(minute_candle):
    url = f"{SPRING_BASE_URL}/minute"
    try:
        res = requests.post(url, json=minute_candle.to_dict(), timeout=5)
        res.raise_for_status()
        logger.info(f"[SUCCESS] Minute data sent: {res.text}")
    except Exception as e:
        logger.error(f"[ERROR] Failed to send minute data: {e}")


def send_daily_data(daily_snapshot):
    url = f"{SPRING_BASE_URL}/daily"
    try:
        res = requests.post(url, json=daily_snapshot.to_dict(), timeout=5)
        res.raise_for_status()
        logger.info(f"[SUCCESS] Daily data sent: {res.text}")
    except Exception as e:
        logger.error(f"[ERROR] Failed to send daily data: {e}")


def send_minute_chart_data(minute_chart_item):
    url = f"{SPRING_BASE_URL}/minute/chart"
    try:
        res = requests.post(url, json=minute_chart_item, timeout=5)
        res.raise_for_status()
        logger.info(f"[SUCCESS] Chart minute data sent: {res.text}")
    except Exception as e:
        logger.error(f"[ERROR] Failed to send chart minute data: {e}")
