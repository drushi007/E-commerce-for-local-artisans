from django.shortcuts import render, HttpResponse, redirect
from store.models import Product, About, info, Category
from store.models import Product1, prices, Signup
from store.models import Customer, Auth, Volunteer,Institute
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class InstituteSignup(View):

    def get(self,request):
        return render(request,"institute.html")

    def post(self,request):
        postData=request.POST
        name=postData.get("name")
        state=postData.get("state")
        city=postData.get("city")
        address=postData.get("address")
        aicte_rank=postData.get("aicte_rank")
        department_no=postData.get("department_no")
        courses_offered=postData.get("courses_offered")
        students_capacity=postData.get("students_capacity")


        values={
            "name":name,
            "state":state,
            "city":city,
            "address":address,
            "aicte_rank":aicte_rank,
            "department_no":department_no,
            "courses_offered":courses_offered,
            "students_capacity":students_capacity
        }

        institute=Institute(name=name,state=state,city=city,address=address,aicte_rank=aicte_rank,
                            department_no=department_no,courses_offered=courses_offered,students_capacity=students_capacity)

        institute.register()
        data1 = {

            'values': values
        }





        return render(request,"institute.html",data1)

