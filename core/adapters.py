"""
Adapters
"""
from abc import ABCMeta, abstractmethod

from twelvedata.api import Api


TWELVE_API_KEY = 'foo'  # TODO: move to os.environ


class AbstractAdapter(metaclass=ABCMeta):
    @abstractmethod
    def get_index_recent_price(self, index):
        pass


class TwelveAdapter(AbstractAdapter):
    def __init__(self, api: Api):
        self._api = api

    def get_index_recent_price(self, index):
        pass


class BitbayAdapter(AbstractAdapter):  # TODO: do it at home guys!
    def __init__(self, api: Api):
        self._api = api

    def get_index_recent_price(self, index):
        pass
