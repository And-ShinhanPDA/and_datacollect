from apscheduler.schedulers.background import BackgroundScheduler
from api.broker_api import get_price_and_volume


def start_scheduler(token: str):
    scheduler = BackgroundScheduler()

    def job():
        result = get_price_and_volume(token)
        if result:
            print(
                f"[{result['time']}] 현재가: {result['price']} / 누적 거래량: {result['volume']}")
        else:
            print("데이터 없음")

    # scheduler.add_job(job, "interval", minutes=1)
    scheduler.add_job(job, "interval", seconds=1)
    scheduler.start()
