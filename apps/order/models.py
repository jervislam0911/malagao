from django.db import models
from datetime import datetime
from product.models import Product
from users.models import AbstractUser
# Create your models here.


# Order
class Order(models.Model):
    STATUS_CHOICES = (
        ("completed", "completed"),
        ("cancel", "cancel"),
        ("shipped", "shipped"),
    )
    product = models.ForeignKey(Product, verbose_name="product")
    user = models.ForeignKey(AbstractUser, verbose_name="user")
    shipping_address = models.CharField(max_length=20, verbose_name="shipping address")
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="amount")
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, verbose_name="status")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="created at")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="updated at")

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = verbose_name

