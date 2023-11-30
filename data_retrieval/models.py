from django.db import models
from core_app.models import Symbol

class Prices(models.Model):
    ticker = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    trade_date = models.DateField()
    open_price = models.DecimalField(max_digits=20, decimal_places=2)
    high_price = models.DecimalField(max_digits=20, decimal_places=2)
    low_price = models.DecimalField(max_digits=20, decimal_places=2)
    close_price = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.IntegerField()

    class Meta:
        verbose_name_plural = 'prices'

class Company(models.Model):
    ticker = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    cik = models.IntegerField()
    sector = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'company'