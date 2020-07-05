from unittest import TestCase

from core.adapters import TwelveAdapter
from twelvedata.api import Api


class MockResponse:
    pass


class AdapterTestCase(TestCase):

    def test_adapter_init(self):
        apikey = 'test_api_key'
        api = Api('xyz')
        TwelveAdapter(api)

    def test_adapter_get_index_recent_price(self):
        class FakeApi:
            fake_data = {
                'XYZ': {
                    'values': [
                        {"datetime": "2020-07-02 15:59:00", "open": "364.31000",
                         "high": "364.85001", "low": "364.14001",
                         "close": "364.22000", "volume": "0"}
                    ],
                },
            }

            def get(self, endpoint, index):
                def json(body):
                    return self.fake_data[index]
                response = MockResponse()
                response.status_code = 200
                response.json = json
                return response

        adapter = TwelveAdapter(FakeApi())

        values = adapter.get_index_recent_price('XYZ')
        self.assertEqual(
            ['364.22000', '2020-07-02 15:59:00'],
            values
        )
