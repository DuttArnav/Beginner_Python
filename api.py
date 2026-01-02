import requests
url="https://newsapi.org/"
def fetch_news(api_key, query, page_size=10):
    endpoint = f"{url}v2/everything"
    params = {
        'q': query,
        'pageSize': page_size,
        'apiKey': api_key
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
        