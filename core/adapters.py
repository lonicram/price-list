from abc import ABCMeta, abstractmethod

from twelvedata.api import Api
"""
Adapters
"""

TWELVE_API_KEY = 'foo' # TODO: move to os.environ


class AbstractAdapter(metaclass=ABCMeta):
    @abstractmethod
    def get_index_recent_price(self, index):
        pass


class TwelveAdapter(AbstractAdapter):
    def __init__(self, api: Api):
        self._api = api

    def get_index_recent_price(self, index):
        pass
