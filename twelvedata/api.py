import requests


BASE_URL = 'http://example.com'


class Response:
    def __init__(self):
        pass


class Api:

    def __init__(self, api_key):
        self._api_key = api_key
        self._base_url = BASE_URL

    def _build_endpoint_url(self, endpoint):
        return f"{self._base_url}/{endpoint}"

    def get(self, endpoint, index_name):
        url = self._build_endpoint_url(endpoint)
        response = requests.get(url, params={"symbol": index_name})
        return response
