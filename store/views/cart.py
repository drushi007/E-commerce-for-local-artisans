from django.contrib.auth.hashers import make_password, check_password
from store.models import Customer
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from store.models.products import Product
class Cart(View):
 def get(self,request):
     ids=list(request.session.get('cart').keys())
     products=Product.get_products_by_id(ids)
     print(products)
     return render(request, 'cart.html',{'products':products})




