from django.views.generic import CreateView

from orders.forms import OrderForm


class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm

