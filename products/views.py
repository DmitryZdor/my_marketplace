from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from products.models import Product, ProductCategory, ShoppingCart


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'TOPS_CROPS'


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'TOPS_CROPS - Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context


@login_required
def shopping_cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    shopping_carts = ShoppingCart.objects.filter(user=request.user,
                                                product=product)
    if not shopping_carts.exists():
        ShoppingCart.objects.create(user=request.user, product=product,
                                    quantity=1)
    else:
        shopping_cart = shopping_carts.first()
        shopping_cart.quantity += 1
        shopping_cart.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def shopping_cart_remove(request, shopping_cart_id):
    shopping_cart = ShoppingCart.objects.get(id=shopping_cart_id)
    shopping_cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
