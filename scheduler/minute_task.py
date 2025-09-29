from apscheduler.schedulers.background import BackgroundScheduler
from api.broker_api import get_price_and_volume
from config import STOCK_CODES
import time


def start_scheduler(token: str):
    scheduler = BackgroundScheduler()

    def job():
        for code in STOCK_CODES:
            result = get_price_and_volume(token, stock_code=code)
            if result:
                print(
                    f"[{code}] 현재가: {result['price']} / 누적 거래량: {result['volume']}")
            else:
                print(f"⚠️ 데이터 없음: {code}")
            time.sleep(1)

    # 매 분 정각 실행
    scheduler.add_job(job, "cron", second=0)

    # 테스트: 60초마다 실행
    # scheduler.add_job(job, "interval", seconds=60)

    scheduler.start()
