from http import HTTPStatus

import stripe
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, TemplateView

from common.views import TitleMixin
from orders.forms import OrderForm
from store import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Store - Спасибо за заказ!'

class CanceledTemplateView(TemplateView):
    template_name = 'orders/canceled.html'
    title = 'Store - Заказ отменен!'


class OrderCreateView(TitleMixin,CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Store - Оформление заказа'

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1N6wbvCtFZyAUk5yLLPiMVYI',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_canceled')),
        )
        return  HttpResponseRedirect(checkout_session.url,status = HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)

@csrf_exempt
def stripe_webhook_view(request):
  payload = request.body
  print(payload)
  return HttpResponse(status=200)
