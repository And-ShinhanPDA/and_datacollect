from apscheduler.schedulers.background import BackgroundScheduler
from api.broker_api import get_price_and_volume
from config import STOCK_CODES
import time
import logging

from model.candle import MinuteCandle
from publisher.data_publisher import send_minute_data

logger = logging.getLogger(__name__)


def start_scheduler(token: str):
    scheduler = BackgroundScheduler()

    def job():
        for code in STOCK_CODES:
            result = get_price_and_volume(token, stock_code=code)
            if result:
                candle = MinuteCandle(
                    symbol=code,
                    price=result["price"],
                    volume=result["volume"]
                )
                logger.info(f"[MinuteTask] Collected: {candle}")
                send_minute_data(candle)
            else:
                logger.warning(f"⚠️ 데이터 없음: {code}")
            time.sleep(1)

    # 매 분 정각 실행
    scheduler.add_job(job, "cron", second=0)

    scheduler.start()
