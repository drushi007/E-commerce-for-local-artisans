
from store.models import Customer, Auth, Artisans


from django.contrib.auth.hashers import make_password, check_password

from django.shortcuts import render, HttpResponse, redirect
from django.views import View
class Login_Artisans(View):
 def get(self,request):
        return render(request, 'login.html')
 def post(self,request):

    email = request.POST.get('email')
    password = request.POST.get('password')
    artisans = Artisans.get_artisans_by_email(email)
    print(artisans)
    print(email, password)

    error_message = None
    if artisans:
        flag = check_password(password, artisans.password)
        print(flag)
        if flag:

            request.session['artisan_id'] = artisans.id
            request.session['email'] = artisans.email
            request.session['name'] = artisans.name
            request.session['age'] = artisans.age
            request.session['state'] = artisans.state
            request.session['city'] = artisans.city
            request.session['address'] = artisans.address
            request.session['pincode'] = artisans.pincode
            request.session['contact'] = artisans.contact
            request.session['status'] = artisans.status

            if( request.session['status']):
                print("yes")
                return redirect('artisans_page')
            else:
                error_message="You are not yet approved as seller"
                return render(request, 'login.html', {'error4': error_message, "email": email})















        else:
            error_message = 'Email or Password invalid'

    else:

        error_message = 'Email or Password invalid'
    return render(request, 'login.html', {'error4': error_message, "email": email})
def artisans_logout(request):
    request.session.clear()
    return redirect('Artisans Login')