from django.db import models

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория товаров'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']

    def __str__(self):
        return f'Товар: {self.name} <> Категория {self.category.name}'


class ShoppingCartQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(shopping_cart.sum() for shopping_cart in self)

    def total_quantity(self):
        return sum(shopping_cart.quantity for shopping_cart in self)


class ShoppingCart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    objects = ShoppingCartQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для: {self.user.username} <> Продукт: {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def de_json(self):
        shopping_cart_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum()),
        }
        return shopping_cart_item
