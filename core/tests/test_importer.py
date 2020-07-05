"""
Test importer module
"""
from unittest import TestCase, skip

from core.importer import Importer, TWELVEDATA_SOURCE
from core.adapters import TwelveAdapter


class ImporterTestCase(TestCase):

    def test_loading_config(self):
        test_config = ['AAPL', 'aapl']

        importer = Importer(test_config)

        self.assertEqual(
            {
                'AAPL': TwelveAdapter,
            },
            importer.get_config()
        )

    def test_importing_prices_from_config(self):
        class FakeAdapter:
            def get_index_recent_price(self, index):
                return index, 1.0

        test_config = ['ZZZ', 'yyy']
        importer = Importer(
            test_config,
            indexes_config={
                'ZZZ': 'FakeSource',
                'YYY': 'FakeSourceJPY',
            },
            api_sources_conf={
                'FakeSource': FakeAdapter,
                'FakeSourceJPY': FakeAdapter,
            },
            currency_config={
                'FakeSource': 'USD',
                'FakeSourceJPY': 'JPY',
            }
        )

        indexes_data = importer.fetch_indexes_data()

        self.assertEqual(
            [
                ('YYY', 1.0, 'JPY', 'FakeSourceJPY'),
                ('ZZZ', 1.0, 'USD', 'FakeSource'),
            ],
            list(indexes_data),
        )

    @skip('Only to be run manually')
    def test_integration_with_twelvedata(self):
        test_config = ['AAPL']
        importer = Importer(
            test_config,
        )
        indexes_data = importer.fetch_indexes_data()

        self.assertGreater(
            len(list(indexes_data)),
            0,
        )

    def test_importing_single_price(self):
        pass
        # importer = Importer()
        # importer.load_data()
            # for i in indexes_from_mapper:
                # importer.load_data_for_index(INDEX, SOURCE)
                    # twelve_adapter.get_values(index) - get from mapper
                        # js = api.get_json_from_source(index) -- api.get()
                    # pricesmodel.object.create(values)
