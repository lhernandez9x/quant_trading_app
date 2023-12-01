from django.db import models

class Symbol(models.Model):
    ticker = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.ticker

    class Meta():
        verbose_name_plural = 'symbol'
