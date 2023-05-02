from django.contrib import admin
from products.models import Product, ProductCategory



admin.site.register(ProductCategory)


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', ('name', 'category'), 'description', ('price', 'quantity'))
    readonly_fields = ('description',)
    ordering = ('price', )