import os
from dotenv import load_dotenv

load_dotenv()

APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")
BASE_URL = os.getenv(
    "BASE_URL", "https://openapivts.koreainvestment.com:29443")

STOCK_CODES = [
    "005930",  # 삼성전자
    "000660",  # SK하이닉스
    "373220",  # LG에너지솔루션
    "012450",  # 한화에어로스페이스
    "005380",  # 현대차
    "105560",  # KB금융
    "035420",  # NAVER
    "329180",  # HD현대중공업
    "068270",  # 셀트리온
    "034020",  # 두산에너빌리티
    "000270",  # 기아
    "055550",  # 신한지주
    "035720",  # 카카오
    "086790",  # 하나금융지주
    "015760",  # 한국전력
    "005490",  # POSCO홀딩스
    "011200",  # HMM
    "138040",  # 메리츠금융지주
    "316140",  # 우리금융지주
    "010130",  # 고려아연
]
