from django.db import models

from .artisans import Artisans
from .products import Product
from .customer import Customer
import datetime




class Order(models.Model) :
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=200,default='',blank=True)
    phone=models.CharField(max_length=15,default='',blank=True)
    pincode=models.CharField(max_length=10,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    order_placed=models.BooleanField(default=False)
    order_processed = models.BooleanField(default=False)
    order_shipped = models.BooleanField(default=False)
    order_delivered = models.BooleanField(default=False)
    artisan_name=models.CharField(max_length=200,default='')
    artisan_id=models.ForeignKey(Artisans,on_delete=models.CASCADE,default=1)




    def PlaceOrder(self):
           self.save()
    @staticmethod
    def get_orders_by_customer(customer_id):
      return  Order\
          .objects\
          .filter(customer_id=customer_id)\
          .order_by('-date')

    @staticmethod
    def get_orders_by_id(id):
        return Order \
            .objects \
            .filter(artisan_id=id) \
            .order_by('-date')
    def pin(self):
        return Order.objects.get('pincode')

