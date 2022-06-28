from django.contrib.auth.hashers import make_password, check_password
from store.models import Customer
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from store.models.products import Product
from store.models.orders import Order

class Orders(View):
    def get(self,request):
         customer=request.session.get('customer_id')
         print(customer)
         orders=Order.get_orders_by_customer(customer)
         print(orders)


         return render(request,"orders.html",{'orders':orders})