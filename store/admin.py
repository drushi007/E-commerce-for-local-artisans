from django.contrib import admin
from .models import Product
from .models import Category
from .models import About
from .models import info
from .models import prices,Product1,Signup,Customer,Auth,Volunteer,Order,Feedback,Institute,Artisans,Shipment


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category','prices1']

class AdminArtisans(admin.ModelAdmin):
        list_display = ['name', 'email', 'product_name']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminUser(admin.ModelAdmin):
    list_display = ['name', 'email', 'number']

class AdminShpiment(admin.ModelAdmin):
    list_display = ['company_name', 'edd', 'order_id']

class AdminInfo(admin.ModelAdmin):
    list_display = ['name']
class Adminprices(admin.ModelAdmin):
    list_display = ['pricerange']
class AdminProduct1(admin.ModelAdmin):
    list_display = ['name','prices1','price']
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone']
class AdminAuth(admin.ModelAdmin):
    list_display = ['name']
class  AdminVoln(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone','state','city','pincode']
class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','quantity','price','date','pincode']
class AdminFeedback(admin.ModelAdmin):
    list_display = ['name','email','phone','rating']

class AdminInstitute(admin.ModelAdmin):
    list_display = ['name', 'state', 'city','address']




# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(About, AdminUser)
admin.site.register(info,AdminInfo)
admin.site.register(prices,Adminprices)
admin.site.register(Product1,AdminProduct1)
admin.site.register(Signup)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Auth,AdminAuth)
admin.site.register(Volunteer,AdminVoln)
admin.site.register(Order,AdminOrder)
admin.site.register(Feedback,AdminFeedback)
admin.site.register(Institute,AdminInstitute)
admin.site.register(Artisans,AdminArtisans)
admin.site.register(Shipment,AdminShpiment)


