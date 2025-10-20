import requests
from config import APP_KEY, APP_SECRET, BASE_URL
from service.auth_service import get_access_token

API_PATH = "/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice"


def get_daily_summary(token: str, stock_code: str = "005930"):
    url = BASE_URL + API_PATH
    headers = {
        "authorization": f"Bearer {token}",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        "tr_id": "FHKST03010100",  # 일봉 조회용
    }
    params = {
        "FID_COND_MRKT_DIV_CODE": "J",
        "FID_INPUT_ISCD": stock_code,
        "FID_INPUT_DATE_1": "20240101",
        "FID_INPUT_DATE_2": "20240101",
        "FID_PERIOD_DIV_CODE": "D",
        "FID_ORG_ADJ_PRC": "0",
    }

    res = requests.get(url, headers=headers, params=params)
    data = res.json()
    # print("📡 API Raw Response:", data)

    if "output1" in data:
        return {
            "prev_close": data["output1"].get("stck_prdy_clpr"),
            "prev_volume": data["output1"].get("prdy_vol"),
            "today_open": data["output1"].get("stck_oprc"),
            "low_52w": data["output1"].get("stck_llam"),
            "high_52w": data["output1"].get("stck_mxpr"),
        }
    else:
        print("⚠️ API 응답 이상:", data)
        return None
