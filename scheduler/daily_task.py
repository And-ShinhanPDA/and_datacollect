from apscheduler.schedulers.background import BackgroundScheduler
from api.daily_api import get_daily_summary
from config import STOCK_CODES
import time
import logging

from model.snapshot import DailySnapshot
from publisher.data_publisher import send_daily_data

logger = logging.getLogger(__name__)


def start_daily_scheduler(token: str):
    scheduler = BackgroundScheduler()

    def job():
        for code in STOCK_CODES:
            result = get_daily_summary(token, stock_code=code)
            if result:
                snapshot = DailySnapshot(
                    symbol=code,
                    prevClose=result["prev_close"],
                    prevVolume=result["prev_volume"],
                    openPrice=result["today_open"],
                    high52w=result["high_52w"],
                    low52w=result["low_52w"]
                )
                logger.info(f"[DailyTask] Collected: {snapshot}")
                send_daily_data(snapshot)
            else:
                logger.warning(f"⚠️ 데이터 없음: {code}")
            time.sleep(1)

    # 테스트: 30초마다 실행
    scheduler.add_job(job, "interval", seconds=30)
    # 실제 운영: 매일 9시 정각
    # scheduler.add_job(job, "cron", hour=9, minute=0, second=1)

    scheduler.start()
