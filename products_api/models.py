from django.db import models


class Product(models.Model):

    product_name = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=100)

