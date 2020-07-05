"""
Adapters
"""
import os
from abc import ABCMeta, abstractmethod

from twelvedata.api import Api


TWELVE_API_KEY = os.environ['TWELVE_API_KEY']


class AbstractAdapter(metaclass=ABCMeta):
    @abstractmethod
    def get_index_recent_price(self, index):
        pass


class TwelveAdapter(AbstractAdapter):
    ENDPOINT_TIME_SERIES = 'time_series'

    def __init__(self, api: Api = None):
        self._api = Api(TWELVE_API_KEY) if api is None else api

    def get_index_recent_price(self, index):
        response = self._api.get(self.ENDPOINT_TIME_SERIES, index)
        json_data = response.json()
        return json_data['values'][0]['close'], json_data['values'][0]['datetime']


class BitbayAdapter(AbstractAdapter):  # TODO: do it at home guys!
    def __init__(self, api: Api):
        self._api = api

    def get_index_recent_price(self, index):
        pass
