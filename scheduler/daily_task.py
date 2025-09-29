from apscheduler.schedulers.background import BackgroundScheduler
from api.daily_api import get_daily_summary


def start_daily_scheduler(token: str):
    scheduler = BackgroundScheduler()

    def job():
        result = get_daily_summary(token)
        if result:
            print(
                f"[일별 요약] 전날 종가: {result['prev_close']} / "
                f"전날 거래량: {result['prev_volume']} / "
                f"오늘 시가: {result['today_open']} / "
                f"52주 최저가: {result['low_52w']} / "
                f"52주 최고가: {result['high_52w']}"
            )
        else:
            print("데이터 없음")

    # 테스트: 1초마다 실행
    scheduler.add_job(job, "interval", seconds=1)
    scheduler.start()
