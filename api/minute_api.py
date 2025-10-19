import requests
from config import APP_KEY, APP_SECRET, BASE_URL

API_PATH = "/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice"


def get_minute_for_chart(token: str, stock_code: str, time: str):
    url = BASE_URL + API_PATH
    headers = {
        "authorization": f"Bearer {token}",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        "tr_id": "FHKST03010200"
    }
    params = {
        "FID_COND_MRKT_DIV_CODE": "J",  # 주식시장
        "FID_INPUT_ISCD": stock_code,   # 종목코드
        "FID_INPUT_HOUR_1": time,   # 조회 시작 시각 (HHMM)
        "FID_ETC_CLS_CODE": "00",
        "FID_PW_DATA_INCU_YN": "Y"
    }

    res = requests.get(url, headers=headers, params=params)
    data = res.json()

    if "output2" in data and isinstance(data["output2"], list) and len(data["output2"]) > 0:
        item = data["output2"][0]

        date = item.get("stck_bsop_date")
        hour = item.get("stck_cntg_hour")
        price = item.get("stck_prpr")
        open_p = item.get("stck_oprc")
        high = item.get("stck_hgpr")
        low = item.get("stck_lwpr")
        volume = item.get("cntg_vol")
        total_value = item.get("acml_tr_pbmn")

        print(
            f"🕒 [{stock_code}] {date} {hour} | 시가:{open_p}, 고가:{high}, 저가:{low}, 종가:{price}, "
            f"거래량:{volume}, 거래대금:{total_value}"
        )

        return item

    else:
        print(f"⚠️ {stock_code} output2 데이터 없음")
        return None
