USD_CURRENCY = 'USD'
TWELVEDATA_SOURCE = 'twelvedata'
BITBAY_SOURCE = 'bitbay'
SOURCE_CHOICES = (
    (TWELVEDATA_SOURCE, 'twelvedata'),
)
APPLE_INDEX = 'AAPL'
BTC_INDEX = 'btc'
INDEX_NAME_CHOICES = (
    (APPLE_INDEX, 'apple'),
    (BTC_INDEX, 'btc'),
)
STOCKS_CATEGORY = 'stocks'
COMMODITIES_CATEGORY = 'commodities'
CURRENCIES_CATEGORY = 'currencies'
CATEGORY_CHOICES = (
    (STOCKS_CATEGORY, 'stocks'),
    (COMMODITIES_CATEGORY, 'commodities'),
    (CURRENCIES_CATEGORY, 'currencies'),
)