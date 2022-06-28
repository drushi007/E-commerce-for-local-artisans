from django.contrib.auth.hashers import make_password, check_password
from store.models import Customer
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from store.models.products import Product
from store.models.orders import Order

class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        pincode=request.POST.get("pincode")
        request.session['pincode']=pincode
        request.session['address']=address
        customer=request.session.get("customer_id")
        phone=request.POST.get("phone")

        cart=request.session.get('cart')
        products= Product.get_products_by_id(list(cart.keys()))
        print(address,pincode,customer,phone,cart,products)

        for product in products:
            artisan_name= product.artisans_name.name
            print(cart.get(str(product.id)))
            order=Order(customer=Customer(id=customer),product=product,artisan_name=artisan_name,
                        address=address,phone=phone,pincode=pincode,
                        price=product.price,quantity=cart.get(str(product.id)))
            print(order.PlaceOrder())
        request.session['cart']={}
        return redirect('cart')