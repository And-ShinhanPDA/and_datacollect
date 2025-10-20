import requests
from config import APP_KEY, APP_SECRET, BASE_URL

API_PATH = "/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice"


def get_price_and_volume(token: str, stock_code: str = "005930"):
    url = BASE_URL + API_PATH
    headers = {
        "authorization": f"Bearer {token}",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        "tr_id": "FHKST03010200"   # 시세 조회용 거래ID (모의투자)
    }
    params = {
        "FID_COND_MRKT_DIV_CODE": "J",  # 주식시장
        "FID_INPUT_ISCD": stock_code,   # 종목코드
        "FID_INPUT_HOUR_1": "0900",     # 조회 시작 시각 (HHMM)
        "FID_ETC_CLS_CODE": "00",
        "FID_PW_DATA_INCU_YN": "Y"
    }

    res = requests.get(url, headers=headers, params=params)
    data = res.json()
    # print("📡 API Raw Response:", data)

    if "output2" in data and len(data["output2"]) > 0:
        return {
            "price": data["output1"].get("stck_prpr"),
            "volume": data["output1"].get("acml_vol"),

        }

    else:
        print("⚠️ API 응답 이상:", data)
        return None
