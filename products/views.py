from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, ShoppingCart
from users.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'title': 'TOPS_CROPS',

    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'TOPS_CROPS - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)


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