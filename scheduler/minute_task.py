import pytz
from datetime import datetime, timedelta, time as dtime
from apscheduler.schedulers.background import BackgroundScheduler
from api.broker_api import get_price_and_volume
from api.minute_api import get_minute_for_chart
from config import STOCK_CODES
import time
import logging

from model.candle import MinuteCandle
from publisher.data_publisher import send_minute_data
from publisher.data_publisher import send_minute_chart_data

KST = pytz.timezone("Asia/Seoul")

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
                # print("job1 실행")
                send_minute_data(candle)
            else:
                logger.warning(f"⚠️ 데이터 없음: {code}")
            time.sleep(1)

    # 매 분 정각 실행
    scheduler.add_job(job, "cron", second=2)

    # scheduler.start()

    def job2():
        # print("job2 시작")
        now = datetime.now(KST)
        if not (dtime(9, 0) <= now.time() <= dtime(15, 31)):
            logger.info(f"[{now.strftime('%H:%M:%S')}] 장 외 시간 - 요청 스킵")
            return

        target_time = (now - timedelta(minutes=1)).strftime("%H%M%S")

        for code in STOCK_CODES:
            try:
                logger.info(f"📡 {code} - {target_time} 시각 데이터 요청 중")
                print(f"📡 {code} - {target_time} 시각 데이터 요청 중")
                result = get_minute_for_chart(
                    token, stock_code=code, time=target_time)

                if result:
                    result["stock_code"] = code
                    print(result)
                    send_minute_chart_data(result)
                else:
                    logger.warning(f"⚠️ {code} 데이터 없음")

                time.sleep(1)

            except Exception as e:
                logger.error(f"❌ {code} 요청 실패: {e}")
                time.sleep(1)

    scheduler.add_job(job2, "cron", second=30)

    scheduler.start()
