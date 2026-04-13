import requests
import time


BASE_URL = "https://newsapi.org/v2/"


def _make_request(endpoint, api_key, params):
    url = BASE_URL + endpoint

    params_final = params.copy()
    params_final["apiKey"] = api_key

    for _ in range(3):
        try:
            response = requests.get(url, params=params_final, timeout=30)

            if response.status_code != 200:
                raise Exception(f"HTTP {response.status_code}: {response.text}")

            return response.json()

        except requests.exceptions.RequestException:
            time.sleep(2)

    raise Exception(f"Ошибка при запросе к NewsAPI {endpoint}")


def get_top_headlines(api_key, **params):
    return _make_request("top-headlines", api_key, params)