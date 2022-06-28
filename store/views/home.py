from django.shortcuts import render, HttpResponse, redirect
from store.models import Product, About, info, Category
from store.models import Product1, prices, Signup
from store.models import Customer, Auth, Volunteer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
class Index(View):
    def post(self, request):

        product = request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity :
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
        request.session['cart']=cart
        print(request.session['cart'])

        return redirect('home')
    def get(self,request):
        cart=request.session.get('cart')



        if not cart:
            request.session['cart'] = {}
        products = None


        data = {}

        # filter by category
        categories = Category.get_all_category()
        categoryID = request.GET.get('category')

        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()

        data['products'] = products
        data['categories'] = categories



        return render(request, 'index.html', data)




