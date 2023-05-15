from django.urls import path

from products.views import ProductsListView, shopping_cart_add, shopping_cart_remove
from django.views.decorators.cache import cache_page

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='main'),
    path('category/<int:category_id>/', cache_page(20)(ProductsListView.as_view()), name='category'),
    path('shopping_carts/add/<int:product_id>/',
         shopping_cart_add, name='shopping_cart_add'),
    path('shopping_carts/remove/<int:shopping_cart_id>/',
         shopping_cart_remove, name='shopping_cart_remove'),
]
