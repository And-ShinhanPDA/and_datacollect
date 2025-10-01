from apscheduler.schedulers.background import BackgroundScheduler
from api.daily_api import get_daily_summary
from config import STOCK_CODES
import time


def start_daily_scheduler(token: str):
    scheduler = BackgroundScheduler()

    def job():
        for code in STOCK_CODES:
            result = get_daily_summary(token, stock_code=code)
            if result:
                print(
                    f"[{code}] "
                    f"[일별 요약] 전날 종가: {result['prev_close']} / "
                    f"전날 거래량: {result['prev_volume']} / "
                    f"오늘 시가: {result['today_open']} / "
                    f"52주 최저가: {result['low_52w']} / "
                    f"52주 최고가: {result['high_52w']}"
                )
            else:
                print("데이터 없음")
            time.sleep(1)

    # 테스트: 1초마다 실행
    scheduler.add_job(job, "interval", seconds=30)
    # scheduler.add_job(job, "cron", hour=9, minute=0, second=1)

    scheduler.start()
