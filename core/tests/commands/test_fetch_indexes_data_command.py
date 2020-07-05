from unittest.mock import patch, MagicMock

from django.core.management import call_command
from django.test import TestCase

from core.models import Price, Currency, Source, Index
import core.importer as importer


class FetchIndexesDataTestCase(TestCase):
    def setUp(self) -> None:
        Currency.objects.create(
            name='USD',
        )
        Source.objects.create(
            name='twelvedata',
            url='example.com'
        )
        Index.objects.create(
            name='XYZ',
            category='test',
        )

    @patch.object(importer, 'Importer')
    def test_fetch_indexes_data(self, importer_mock):
        """ Test if downloaded prices have been loaded to db"""
        args = ['XYZ']
        opts = {}

        self.assertEqual(Price.objects.count(), 0)
        test_indexes_data = ('1.0', '2020-07-02 15:30:00', 'USD', 'twelvedata', 'XYZ')
        importer_mock.return_value.fetch_indexes_data = MagicMock(return_value=test_indexes_data)
        call_command('fetch_indexes_data', *args, **opts)

        prices = Price.objects.all()
        price_entry = prices.first()
        self.assertEqual(
            (price_entry.value, price_entry.currency.name),
            (1.0, 'USD'),
        )
