from fastapi import FastAPI
from scheduler.minute_task import start_scheduler
from scheduler.daily_task import start_daily_scheduler
from service.auth_service import get_access_token
import requests

app = FastAPI()

# SPRING_URL = "http://localhost:8082/api/test/ping"
SPRING_URL = "http://43.203.153.18/process/api/test/ping"


@app.get("/ping-to-spring")
def ping_to_spring():
    """Swagger에서 호출 → Spring 서버에 요청 → 응답 반환"""
    try:
        res = requests.get(SPRING_URL)
        return {"spring_response": res.text, "status_code": res.status_code}
    except Exception as e:
        return {"error": str(e)}


@app.on_event("startup")
def startup_event():
    token = get_access_token()
    start_scheduler(token)
    start_daily_scheduler(token)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
