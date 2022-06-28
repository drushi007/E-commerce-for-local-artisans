from django.db import models
from .category import Category
from .product1 import prices
from .artisans import Artisans


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    prices1 = models.ForeignKey(prices, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/artisans_product')
    description = models.CharField(max_length=500)
    artisans_name=models.ForeignKey(Artisans,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_all_products_by_priceid(prices1_id):
        if prices1_id:
            return Product.objects.filter(prices1=prices1_id)
        else:
            return Product.get_all_products()