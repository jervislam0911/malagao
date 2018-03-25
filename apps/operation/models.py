from django.db import models

# Create your models here.
from datetime import datetime

from users.models import UserProfile
from product.models import Product


class ProductComments(models.Model):
    product = models.ForeignKey(Product, verbose_name="product")
    user = models.ForeignKey(UserProfile, verbose_name="user")
    comments = models.CharField(max_length=250, verbose_name="comments")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="created at")

    class Meta:
        verbose_name = "product comments"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    TYPE_CHOICES = (
        (1, "product"),
        (2, "category"),
    )

    user = models.ForeignKey(UserProfile, verbose_name="user")
    # course = models.ForeignKey(Course, verbose_name=u"课程")
    # teacher = models.ForeignKey()
    # org = models.ForeignKey()
    # fav_type =

    fav_id = models.IntegerField(default=0)
    fav_type = models.IntegerField(
        choices=TYPE_CHOICES,
        default=1,
        verbose_name="favorite type")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="created at")

    class Meta:
        verbose_name = "user favorite"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name="user")
    message = models.CharField(max_length=500, verbose_name="message")
    has_read = models.BooleanField(default=False, verbose_name="has read")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="created at")

    class Meta:
        verbose_name = u"user message"
        verbose_name_plural = verbose_name


class UserProduct(models.Model):
    product = models.ForeignKey(Product, verbose_name="product")
    user = models.ForeignKey(UserProfile, verbose_name="user")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="created at")

    class Meta:
        verbose_name = "user product"
        verbose_name_plural = verbose_name
