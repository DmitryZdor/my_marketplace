from django.db import models

from users.models import User


class Order(models.Model):
    CREATED = 0
    WAIT_FOR_PAY = 1
    PAID = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (WAIT_FOR_PAY, 'Ожидает оплаты'),
        (PAID, 'Оплачен'),
        (DELIVERED, 'Доставлен'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=255)
    shopping_cart_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order # {self.id}. {self.first_name} {self.last_name}'
