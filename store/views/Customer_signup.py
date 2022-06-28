from django.shortcuts import render, HttpResponse, redirect
from store.models import Product, About, info, Category
from store.models import Product1, prices, Signup
from store.models import Customer, Auth, Volunteer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

#customer registration

class customer_signup(View):
    def get(self,request):
        sign = Signup.get_all_images()
        return render(request, "signup.html", {'sign': sign})
    def validateCustomer(self,customer):
        error_message = None
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:

            error_message = "First Name must be 4 characters or more !"
        elif not customer.last_name:
            error_message = 'Last Name Required '
        elif len(customer.last_name) < 4:
            error_message = "Last Name must be 4 characters or more !"
        elif not customer.email:
            error_message = "Please Enter E-mail"
        elif len(customer.email) < 5:
            error_message = "Please Enter Valid  E-mail"
        elif not customer.phone:
            error_message = "Phone Number required"
        elif len(customer.phone) < 10:
            error_message = "Phone Number Must contain 10 characters or more"
        elif not customer.password:
            error_message = "Enter a Valid Password"
        elif len(customer.password) < 6:
            error_message = "Password must be at least 6 characters long"
        elif not customer.re_enter:
            error_message = "Enter a Valid Password"
        elif len(customer.re_enter) < 6:
            error_message = "Enter a Valid Password"
        elif customer.password != customer.re_enter:
            error_message = "Your Password Did Not Match"

        elif customer.isExists():
            error_message = 'Email Address Already Registered'
        return error_message
    def post(self,request):
        postData = request.POST
        first_name = postData.get('First Name')
        last_name = postData.get('Last Name')
        email = postData.get('email')
        password = postData.get('password')
        re_enter = postData.get('re-enter password')
        phone = postData.get('Mobile Number')

        values = {
            'First_name': first_name,
            'last_name': last_name,
            'email': email,

            'phone': phone, }
        # Validation


        error_message = None
        customer = Customer(first_name=first_name, last_name=last_name, email=email,
                            password=password, re_enter=re_enter, phone=phone)
        error_message = self.validateCustomer(customer)

        # saving
        if not error_message:

            print(first_name, last_name, email, password, phone)
            customer.password = make_password(customer.password)
            customer.re_enter = make_password(customer.re_enter)

            customer.register()

            return redirect('home')
        else:
            data1 = {
                'error': error_message,
                'values1': values
            }
            return render(request, "signup.html", data1)