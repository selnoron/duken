from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(
        verbose_name='name of product',
        max_length=50,
        unique=True
    )
    price = models.DecimalField(
        verbose_name='price of product',
        decimal_places=2,
        max_digits=30
    )

    class Meta:
        ordering = ('name', 'price')
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Order(models.Model):
    user = models.ForeignKey(
        verbose_name='who ordered',
        to=User,
        related_name='u_orders',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        verbose_name='which product',
        to=Product,
        related_name='p_orders',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'order'
        verbose_name_plural = 'orders'