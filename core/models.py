from django.db import models


class BaseModel(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_created=True)

    class Meta:
        abstract = True


class Currency(BaseModel):
    name = models.CharField(max_length=255)


class Index(BaseModel):
    name = models.CharField(max_length=255)


class Source(BaseModel):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)


class Price(BaseModel):
    category = models.CharField(max_length=255)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    index = models.ForeignKey(Index, on_delete=models.CASCADE)


class PriceAlert(BaseModel):
    type = models.CharField(max_length=255)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
