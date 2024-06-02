import requests
from config import API_KEY, BASE_URL

def get_weather(location):
    url = f"{BASE_URL}/current.json"
    params = {
        'key': API_KEY,
        'q': location
    }
    headers = {
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
