from django.contrib import admin

from products.models import Product, ProductCategory, ShoppingCart

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', ('name', 'category'), 'description', ('price', 'quantity'))
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('price', )


class ShoppingCartAdmin(admin.TabularInline):
    model = ShoppingCart
    fields = ('product', 'quantity', 'create_timestamp')
    readonly_fields = ('create_timestamp',)
    extra = 0
