from django.urls import path

from .views import customer_login,Customer_signup,others,Signup_Artisans,Artisans_Login,home,cart,feedback,artisans_page
from .views.customer_login import customer_logout
from .views.orders import Orders
from .views.Artisans_Login import artisans_logout
from .views.artisans_orders import Artisans_Orders

from .views.Order_Process import Accept_Order,Deliver_Order,Process_Order,order_detail,Shipment_Details,Ship_Order

from .views.order_detail import OrderDetail

from .views.others import Artisan_Profile;
from .views.checkout import Checkout
from .views.Artisans_Login import Login_Artisans
from .views.Signup_Artisans import Artisans_Signup
from .views.institute import InstituteSignup
urlpatterns= [



    path('',home.Index.as_view(),name='home'),
    path('aboutus', others.aboutus, name='aboutus'),
    path('aboutourwebsite', others.infom, name='infom'),
    path('prices',others.Prices.as_view(),name='cost'),
    path('signup', Customer_signup.customer_signup.as_view(), name='signup'),
    path('prod_auth',others.prod_auth, name='prod_auth'),
    path('artisans', Signup_Artisans.Artisans_Signup.as_view(), name='artisans'),
    path('artisans_page', artisans_page.artisans_page, name='artisans_page'),

    path('customerlogin', customer_login.Login_Customer.as_view(), name="customer_login"),
    path('logout',customer_logout,name='customer_logout'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('checkout',Checkout.as_view(),name="Checkout"),
    path('orders',Orders.as_view(),name="orders"),
    path('profile', customer_login.Customer_Profile, name="customer_profile"),
    path('feedback',feedback.Feedbacks.as_view(),name="feedback"),
    path('artisan_profile',others.Artisan_Profile, name="artisan_profile"),
    path('artisans_orders',Artisans_Orders.as_view(),name="artisans_orders"),
    path('artisans_logout', artisans_logout, name='artisans_logout'),
    path('orders/order_detail/<int:id>',order_detail,name="Order Detail"),

    path('artisanslogin',Artisans_Login.Login_Artisans.as_view(),name="Artisans Login"),
    path('artisans_orders/<int:id>', Accept_Order, name="accept_order"),
    path('artisans_orders/procees_order/<int:id>', Process_Order, name="procees_order"),
    path('artisans_orders/shipped/<int:id>', Ship_Order, name="shipped"),
    path('artisans_orders/delivered/<int:id>', Deliver_Order, name="delivered"),
    path('artisans_orders/shipment_details/<int:id>', Shipment_Details, name="shipment_details"),


]
