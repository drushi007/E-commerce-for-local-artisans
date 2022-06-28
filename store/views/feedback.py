from django.contrib.auth.hashers import make_password, check_password
from store.models import Customer,feedback
from store.models import feedback
from store.models.feedback import Feedback
from django.shortcuts import render, HttpResponse, redirect
from django.views import View

from store.models.products import Product
class Feedbacks(View):

        def get(self, request):

            return render(request, "feedback.html")

        def validateFeedback(self, f):
            error_message = None
            if (not f.name):
                error_message = " Name Required !!"
            elif len(f.name) < 4:

                error_message = "First Name must be 4 characters or more !"

            elif not f.email:
                error_message = "Please Enter E-mail"
            elif len(f.email) < 5:
                error_message = "Please Enter Valid  E-mail"
            elif not f.phone:
                error_message = "Phone Number required"
            elif len(f.phone) < 10:
                error_message = "Phone Number Must contain 10 characters or more"
            elif not f.rating:
                error_message = "Enter a Rating"
            elif not f.experience:
                error_message = "Please Describe  Your Experience"
            elif not f.improve:
                error_message = "Please Tell us What we Need To Improve"

            return error_message

        def post(self, request):
            postData = request.POST
            name = postData.get('name')

            email = postData.get('email')
            phone = postData.get('phone')
            rating=postData.get('rating')
            experience=postData.get('experience')

            improve = postData.get('improve')
            values = {
                'name': name,
                'rating': rating,
                'email': email,
                 'experience':experience,
                'improve':improve,
                'phone': phone, }
            # Validation

            error_message = None
            f = Feedback(name=name,  email=email,
                                phone=phone, improve=improve, rating=rating, experience=experience)
            error_message = self.validateFeedback(f)

            # saving
            if not error_message:


                print(improve,name)
                f.register_feedback()
                return redirect('customer_profile')
            else:
                data1 = {
                    'error': error_message,
                    'values1': values
                }
                return render(request, "feedback.html", data1)