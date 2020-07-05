import abc
import requests


BASE_URL = 'http://example.com'


class AbstractApi(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, endpoint: str, index: str) -> requests.Response:
        pass


class Api(AbstractApi):

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
