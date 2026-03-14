import requests

BASE_URL = 'https://newsapi.org/v2'

def _make_request(endpoint: str, api_key: str, params: dict = None) -> dict[str, str]:
    url = f"{BASE_URL}/{endpoint}"
    default_params = {'apiKey' : api_key}

    if params: default_params.update(params)
    
    try:
        response = requests.get(url, params=default_params, timeout=10)
        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise Exception(f'Ошибка при запросе к NewsAPI {endpoint}: {e}')
    
    except ValueError as e:
        raise Exception(f'Ошибка парсинга Json ({endpoint}): {e}')
    

def get_top_headlines(api_key: str, q: str, country: str = None , category: str = None, 
                      sources: str = None, pageSize: int= None, page: int= None) -> dict[str,str]:
    params = {'q': q, 
              'country': country,
              'sources': sources,
              'pageSize': pageSize,
              'page': page}
    
    params_final = {key: value for key, value in params.items() if value is not None}
    return _make_request('top-headlines',api_key, params_final)
        

    
