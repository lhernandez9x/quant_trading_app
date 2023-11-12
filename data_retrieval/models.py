from django.db import models

# Create your models here.

class Symbol(models.Model):
    ticker = models.CharField(max_length=200)

    class Meta():
        verbose_name_plural = 'symbol'

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
