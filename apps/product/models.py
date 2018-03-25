from django.db import models

# Create your models here.
from datetime import datetime


# product
class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="title")
    description = models.CharField(max_length=300, verbose_name="description")
    detail = models.TextField(verbose_name="detail")
    upc_code = models.CharField(max_length=45, verbose_name="upc code")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="created at")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="updated at")
    fav_nums = models.IntegerField(default=0, verbose_name="favorite numbers")
    feature_image = models.ImageField(
        upload_to="product/%Y/%m",
        verbose_name="feature_image",
        max_length=100)

    click_nums = models.IntegerField(default=0, verbose_name="click numbers")
    regular_price = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="regular price")
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="sale price")

    class Meta:
        verbose_name = "product"
        verbose_name_plural = verbose_name


# category
class Category(models.Model):
    product = models.ForeignKey(Product, verbose_name="product")
    title = models.CharField(max_length=100, verbose_name="title")
    description = models.CharField(max_length=300, verbose_name="description")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="created at")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="updated at")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = verbose_name


# image
class Images(models.Model):
    product = models.ForeignKey(Product, verbose_name="product")
    img_name = models.CharField(max_length=100, verbose_name="image name")
    alt_name = models.CharField(max_length=100, verbose_name="alt name")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="created at")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="updated at")
    download = models.FileField(
        upload_to="product/resource/%Y/%m",
        verbose_name=u"image resource",
        max_length=100)

    class Meta:
        verbose_name = "image"
        verbose_name_plural = verbose_name

