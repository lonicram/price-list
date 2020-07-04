from django.contrib import admin
from core.models import PriceAlert, Price, Source, Index, Currency


@admin.register(PriceAlert)
class PriceAlertAdmin(admin.ModelAdmin):
    pass


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    pass


@admin.register(Currency)
class Currency(admin.ModelAdmin):
    pass
