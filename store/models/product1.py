from django.db import models

from .artisans import Artisans


class prices(models.Model):
    pricerange = models.CharField(max_length=200)

    def __str__(self):
        return self.pricerange

    @staticmethod
    def get_all_prices():
        return prices.objects.all()


class Product1(models.Model):
    name = models.CharField(max_length=200)
    prices1 = models.ForeignKey(prices, on_delete=models.CASCADE, default=1)
    price=models.IntegerField(default=0)

    image=models.ImageField(upload_to='uploads/artisans_product',default='')
    artisans_name = models.ForeignKey(Artisans, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_items():
        return Product1.objects.all()



