from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from core.models import Price, Currency, Source, Index
from core.importer import Importer


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('indexes', nargs='+', type=str)

    def handle(self, *args, **options):
        indexes = options['indexes']
        importer = Importer(indexes)
        indexes_data = list(importer.fetch_indexes_data())
        for index_data in indexes_data:
            with transaction.atomic():
                currency, c_created = Currency.objects.get_or_create(name=index_data[2])
                if c_created:
                    currency.save()
                source, s_created = Source.objects.get_or_create(name=index_data[3])
                if s_created:
                    source.save()
                index, i_created = Index.objects.get_or_create(name=index_data[4])
                if i_created:
                    index.save()
                Price.objects.create(
                    value=index_data[0],
                    from_timestamp=index_data[1],
                    currency=currency,
                    source=source,
                    index=index,
                )
        self.stdout.write(self.style.SUCCESS('Successfully synced indexes "%s"' % indexes))
        self.stdout.write(self.style.SUCCESS('Indexes data "%s"' % list(indexes_data)))
