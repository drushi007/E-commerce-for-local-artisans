from django.contrib.auth.hashers import make_password, check_password
from django.views.generic import DetailView

from store.models import Customer
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from store.models.products import Product
from store.models.orders import Order

class Artisans_Orders(View):
    def get(self,request):

        artisan_id=request.session['artisan_id']

        name= request.session['name']


        orders=Order.objects.filter(artisan_id=artisan_id)



        print()

        return render(request,"artisans_order.html",{"orders":orders,"name":name})

