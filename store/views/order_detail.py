from django.views.generic import DetailView
from .orders import Order


class OrderDetail(DetailView):
    template_name = 'order-detail.html'
    context_object_name = 'order'
    model = Order
    def get_queryset(self):
        queryset=Order.objects.filter(id=self.request.id)
        return queryset
