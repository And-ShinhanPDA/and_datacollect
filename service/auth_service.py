import requests
from config import APP_KEY, APP_SECRET, BASE_URL


def get_access_token():
    url = f"{BASE_URL}/oauth2/tokenP"
    data = {
        "grant_type": "client_credentials",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET
    }
    res = requests.post(url, json=data)
    return res.json().get("access_token")
