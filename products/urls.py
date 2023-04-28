from django.urls import path
from products.views import products, shopping_cart_add, shopping_cart_remove

app_name = 'products'

urlpatterns = [
    path('', products, name='main'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('shopping_carts/add/<int:product_id>/',
         shopping_cart_add, name='shopping_cart_add'),
    path('shopping_carts/remove/<int:shopping_cart_id>/',
         shopping_cart_remove, name='shopping_cart_remove'),
    path('category/<int:category_id>/<int:page_number>/', products, name='paginator_category'),
]

