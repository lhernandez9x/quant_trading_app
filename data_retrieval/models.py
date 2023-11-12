from django.db import models

# Create your models here.

class Symbol(models.Model):
    ticker = models.CharField(max_length=200)
