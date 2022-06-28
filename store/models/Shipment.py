from django.db import models

from .artisans import Artisans
from .orders import Order

class Shipment(models.Model):
    company_name = models.CharField(max_length=200 ,default='')
    tracking_id = models.CharField(max_length=200,default='')
    company_contact =models.CharField(max_length=200,default='')
    edd=models.DateTimeField(auto_now_add=False)
    order_id = models.CharField(max_length=50,default='')
