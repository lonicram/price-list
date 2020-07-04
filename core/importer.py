"""
Import prices data from external services
"""
from core.models import TWELVEDATA_SOURCE, BITBAY_SOURCE, BTC_INDEX, APPLE_INDEX
from twelvedata import api

INDEX_SOURCES_MAPPER = {
    APPLE_INDEX: TWELVEDATA_SOURCE,
    BTC_INDEX: BITBAY_SOURCE,
}

API_SOURCES_MAPPER = {
    TWELVEDATA_SOURCE: api.Api,
}


class Importer:
    pass
