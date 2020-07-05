"""
Import prices data from external services
"""
from core.config import TWELVEDATA_SOURCE, BITBAY_SOURCE, BTC_INDEX, APPLE_INDEX, USD_CURRENCY
from core.adapters import TwelveAdapter

INDEXES_CONFIG = {
    APPLE_INDEX: TWELVEDATA_SOURCE,
    BTC_INDEX: BITBAY_SOURCE,
}

CURRENCY_MAPPER = {
    TWELVEDATA_SOURCE: USD_CURRENCY,
}

API_SOURCES_MAPPER = {
    TWELVEDATA_SOURCE: TwelveAdapter,
}


class Importer:

    def __init__(self, indexes, indexes_config=None, api_sources_conf=None, currency_config=None):
        # TODO: refactor config assignment
        self._indexes_conf = INDEXES_CONFIG if indexes_config is None else indexes_config
        self._api_sources_conf = API_SOURCES_MAPPER if api_sources_conf is None else api_sources_conf
        self._currency_config = CURRENCY_MAPPER if currency_config is None else currency_config
        self._indexes = indexes
        self._config = self._load_config(indexes)

    def _load_config(self, indexes):
        config = {}
        for index in set(map(lambda x: x.upper(), indexes)):
            adapter = self._api_sources_conf[self._indexes_conf[index]]
            config[index] = adapter
        return config

    def get_config(self):
        return self._config

    def fetch_indexes_data(self):
        for index, adapter in sorted(self._config.items()):
            value, timestamp = adapter().get_index_recent_price(index)
            source = self._indexes_conf[index]
            yield value, timestamp, self._currency_config[source], source, index,
