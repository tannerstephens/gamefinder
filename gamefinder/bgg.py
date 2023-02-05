import requests

BASE_URL = "https://api.geekdo.com/xmlapi2"


def search(query: str):
    params = {"type": "boardgame", "query": query}
    resp = requests.get(f"{BASE_URL}/search", params=params)
