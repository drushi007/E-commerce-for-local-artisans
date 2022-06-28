from django.shortcuts import render, HttpResponse, redirect
from store.models import Product, About, info, Category
from store.models import Product1, prices, Signup
from store.models import Customer, Auth, Volunteer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

def artisans_page(request):
    return render(request, 'artisans_page.html')