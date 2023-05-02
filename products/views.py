from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, ShoppingCart
from users.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'TOPS_CROPS'
        return context


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['title'] = 'TOPS_CROPS - Каталог'
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