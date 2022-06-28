from django.shortcuts import render, HttpResponse, redirect
from store.models import Product, About, info, Category
from store.models import Product1, prices, Signup
from store.models import Customer, Auth, Volunteer,Artisans
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
# volunteer registration
class Artisans_Signup(View):
  def get(self,request1):
        print("Hi")
        artisans = Artisans.objects.all()
        return render(request1, 'artisans.html', {'artisans': artisans})

  def post(self,request1):
        postData1 = request1.POST
        postData2=request1.FILES
        print("Hello")
        name = postData1.get('name')
        password = postData1.get('password')
        re_enter = postData1.get('re-enter password')
        email = postData1.get('email')

        shop_location=postData1.get('shop_location')
        contact = postData1.get('contact')
        state = postData1.get('state')
        city = postData1.get('city')
        address = postData1.get('address')
        product_name = postData1.get('product_name')
        product_info = postData1.get('product_info')
        product_image = postData2.get('product_image')

        age=postData1.get('age')
        pincode=postData1.get('pincode')
        identity_proof=postData2.get('identity_proof')
        price=postData1.get('price')




        value = {
            'name': name,
            'shop_location': shop_location,
            'email': email,

            'contact': contact,
            'state': state,
            'city': city,
            'address': address,
            'product_name': product_name,
            'product_info': product_info,
            'pincode': pincode,
            'age':age,
            'identity_proof':identity_proof,
            'price':price

        }
        #validation


        error_message1 = None
        artisan = Artisans(name=name, password=password, email=email,
                              re_enter=re_enter, shop_location=shop_location, contact=contact, state=state, city=city,
                              address=address,
                              product_info=product_info,product_name=product_name,product_image=product_image,
                           pincode=pincode, age=age, identity_proof= identity_proof,price=price)

        error_message1 = self.Artisansvalidate(artisan)
        # saving
        if not error_message1:

            artisan.password = make_password(artisan.password)
            artisan.re_enter = make_password(artisan.re_enter)
            artisan.save()
            print("Hey")

            return redirect('home')
        else:
            data = {
                'error1': error_message1,
                'values': value
            }
            return render(request1, 'artisans.html', data)


  def Artisansvalidate(self,artisans):
    error_message1 = None
    if (not artisans.name):
        error_message1 = "Name Required !!"

    elif not artisans.shop_location:
        error_message1 = 'Shop Location Required '

    elif not artisans.email:
        error_message1 = "Please Enter E-mail"
    elif len(artisans.email) < 5:
        error_message1 = "Please Enter Valid  E-mail"
    elif not artisans.contact:
        error_message1 = "Phone Number required"
    elif len(artisans.contact) < 10:
        error_message1 = "Phone Number Must contain 10 characters or more"
    elif not artisans.password:
        error_message1 = "Enter a Valid Password"
    elif len(artisans.password) < 6:
        error_message1 = "Password must be at least 6 characters long"
    elif not artisans.re_enter:
        error_message1 = "Enter a Valid Password"
    elif len(artisans.re_enter) < 6:
        error_message1 = "Enter a Valid Password"
    elif artisans.password != artisans.re_enter:
        error_message1 = "Your Password Did Not Match"
    elif not artisans.state:
        error_message1 = "Enter the State"
    elif not artisans.city:
        error_message1 = "Enter the City"
    elif not artisans.address:
        error_message1 = "Enter the Correct Address"
    elif not artisans.pincode:
        error_message1 = "Enter a Valid Pincode"
    elif not artisans.product_name:
        error_message1 = "Enter the Product Name"
    elif not artisans.product_info:
        error_message1 = "Enter Product Information"






    elif artisans.isExists1():
        error_message1 = 'Email Address Already Registered'
    return error_message1