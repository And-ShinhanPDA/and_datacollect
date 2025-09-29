import os
from dotenv import load_dotenv

load_dotenv()

APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")
BASE_URL = os.getenv(
    "BASE_URL", "https://openapivts.koreainvestment.com:29443")
