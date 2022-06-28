from django.shortcuts import render, redirect

from store.models import Order
from store.models import Shipment





def Accept_Order(request, id):
           print(id)
           q= Order.objects.get(pk=id)
           q.order_placed = True
           q.save()

           artisan_id = request.session['artisan_id']

           name = request.session['name']

           orders = Order.objects.filter(artisan_id=artisan_id)

           return render(request,"artisans_order.html",{"orders":orders})


def Process_Order(request, id):
    print(id)
    q = Order.objects.get(pk=id)
    q.order_processed = True
    q.save()

    artisan_id = request.session['artisan_id']

    name = request.session['name']

    orders = Order.objects.filter(artisan_id=artisan_id)

    return render(request, "artisans_order.html", {"orders": orders})



def Ship_Order(request, id):
    q = Order.objects.get(pk=id)
    q.order_shipped = True
    q.save()


    return render(request,"shipment.html",{"order_id":id})




def Deliver_Order(request, id):
    print(id)
    q = Order.objects.get(pk=id)
    q.order_delivered = True
    q.save()

    artisan_id = request.session['artisan_id']

    name = request.session['name']

    orders = Order.objects.filter(artisan_id=artisan_id)

    return render(request, "artisans_order.html", {"orders": orders})


def order_detail(request,id):
    order = Order.objects.get(pk=id)

    shipment=Shipment.objects.filter(order_id=str(id))
    print(shipment)

    return render(request,"order-detail.html",{"order":order,"shipment":shipment})


def Shipment_Details(request,id):
    q = Order.objects.get(pk=id)
    q.order_shipped = True
    q.save()
    shipment_company = request.POST.get('shipment_company')
    tracking_id = request.POST.get('tracking_id')
    edd=request.POST.get('edd')
    print(edd)
    company_contact=request.POST.get('company_contact')
    artisan_id = request.session['artisan_id']

    error_message=None

    if (not shipment_company):
        error_message = "Company  Name Required !!"
    elif (not tracking_id):

        error_message = "Tracking Id required!"
    elif not edd:
        error_message = 'Estimated Delivery Date Required '
    elif  not company_contact:
        error_message = "Company Contact Required"

    if(not error_message):


          shipment = Shipment(company_name=shipment_company,tracking_id=tracking_id,edd=edd,
                        company_contact=company_contact,order_id =id)


          shipment.save()
          error_message=None

          return  redirect("artisans_orders")


    else:
          return render(request,"shipment.html",{"error":error_message,"order_id":id})





