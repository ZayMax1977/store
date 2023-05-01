from django.views.generic import CreateView

class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'

