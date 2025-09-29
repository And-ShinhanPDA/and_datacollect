from fastapi import FastAPI
from scheduler.minute_task import start_scheduler
from scheduler.daily_task import start_daily_scheduler
from service.auth_service import get_access_token

app = FastAPI()


@app.on_event("startup")
def startup_event():
    token = get_access_token()
    start_scheduler(token)
    start_daily_scheduler(token)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
