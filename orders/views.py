from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from common.views import TitleMixin
from orders.forms import OrderForm
from orders.models import Order
from products.models import ShoppingCart


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'TOPS_CROPS - заказ успешно оформлен'


class OrderDetailView(DetailView):
    template_name = 'orders/order.html'
    model = Order

    def get_context_data(self,**kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['title'] = f'TOPS_CROPS - Заказ #{self.object.id}'
        return context


class OrderListView(TitleMixin, ListView):
    template_name = 'orders/orders.html'
    title = 'TOPS_CROPS - Заказы'
    queryset = Order.objects.all()
    ordering = ('-created',)

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(initiator=self.request.user)


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    title = 'TOPS_CROPS - оформление заказа'
    success_url = reverse_lazy('orders:success')

    # def post(self, request, *args, **kwargs):
    #     super(OrderCreateView, self).post(self, request, *args, **kwargs)
    #     return HttpResponseRedirect(reverse_lazy('orders:success'))
    def form_valid(self, form):
        self.shopping_carts = ShoppingCart.objects.filter(user=self.request.user)
        self.object = form.save(commit=False)
        self.object.status = Order.WAIT_FOR_PAY
        self.object.shopping_cart_history = {
            'purchased_items': [shopping_cart.de_json() for shopping_cart in self.shopping_carts],
            'total_sum': float(self.shopping_carts.total_sum()),
        }
        form.instance.initiator = self.request.user
        self.object.save()
        self.shopping_carts.delete()
        return super(OrderCreateView, self).form_valid(form)
