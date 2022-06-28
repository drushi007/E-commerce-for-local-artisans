from django.contrib.auth.hashers import make_password, check_password
from store.models import Customer
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
class Login_Customer(View):
 def get(self,request):
        return render(request, 'customer_login.html')
 def post(self,request):

    email = request.POST.get('email')
    password = request.POST.get('password')
    customer = Customer.get_customer_by_email(email)
    print(customer)
    print(email, password)

    error_message = None
    if customer:
        flag = check_password(password, customer.password)
        print(flag)
        if flag:
            request.session['customer_id']=customer.id
            request.session['email'] = customer.email
            request.session['first_name'] = customer.first_name

            request.session['last_name'] = customer.last_name
            request.session['phone'] = customer.phone

            print("yes")
            return redirect('home')
        else:
            error_message = 'Email or Password invalid'

    else:

        error_message = 'Email or Password invalid'
    return render(request, 'customer_login.html', {'error4': error_message, "email": email})
def customer_logout(request):
    request.session.clear()
    return redirect('customer_login')
def Customer_Profile(request):


    return render(request,"profile.html")

