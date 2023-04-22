from django.shortcuts import render
from products.models import Product, ProductCategory


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
