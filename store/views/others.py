from django.shortcuts import render, HttpResponse, redirect
from store.models import Product, About, info, Category
from store.models import Product1, prices, Signup
from store.models import Customer, Auth, Volunteer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


# Create your views here.



def aboutus(request):
    abouts = About.about_all_users()
    return render(request, "about.html", {'abouts': abouts})


def infom(request):
    information = info.info_get_all()
    return render(request, "info.html", {'information': information})


class Prices(View):



        def post(self, request):

            product = request.POST.get('product')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity - 1

                    else:
                        cart[product] = quantity + 1
                else:
                    cart[product] = 1

            else:
                cart = {}
                cart[product] = 1
            request.session['cart'] = cart
            print(request.session['cart'])

            return redirect('home')

        def get(self, request):
            cart = request.session.get('cart')
            if not cart:
                request.session['cart'] = {}
            products = None

            data = {}

            # filter by category
            price = prices.get_all_prices()
            priceID = request.GET.get('prices1')

            if priceID:
                products = Product.get_all_products_by_categoryid(priceID)
            else:
                products = Product.get_all_products()

            data['price'] = price
            data['products'] =products

            return render(request, 'prices.html', data)


def prod_auth(request):
    auth = Auth.auth_get_all()
    return render(request, 'product_authentication.html', {'auth': auth})


def Artisan_Profile(request):
    return render(request,'artisans_profile.html')














