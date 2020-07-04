import requests


BASE_URL = 'http://example.com'


class Api:

    def __init__(self, api_key: str):
        self._api_key = api_key
        self._base_url = BASE_URL

    def _build_endpoint_url(self, endpoint: str):
        return f"{self._base_url}/{endpoint}"

    def get(self, endpoint: str, index_name: str) -> requests.Response:
        url = self._build_endpoint_url(endpoint)
        response = requests.get(url, params={
            'symbol': index_name,
            'apikey': self._api_key,
        })
        return response
