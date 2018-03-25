from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        ("male", "male"),
        ("female", "female")
    )

    nick_name = models.CharField(max_length=50, verbose_name="nick name", default="")
    birthday = models.DateField(verbose_name="birthday", null=True, blank=True)
    gender = models.CharField(
        max_length=5,
        verbose_name="gender",
        choices=GENDER_CHOICES,
        default="male")
    address = models.CharField(max_length=100, verbose_name="address", default="")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default="image/default.png",
        max_length=100
    )

    class Meta:
        verbose_name = "user info"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ("register", "register"),
        ("forget", "forget")
    )
    code = models.CharField(max_length=20, verbose_name="verification code")
    email = models.EmailField(max_length=50, verbose_name="email")
    send_type = models.CharField(choices=SEND_CHOICES, max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "email verification code"
        verbose_name_plural = verbose_name

# 轮播图model


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    image = models.ImageField(
        upload_to="banner/%Y/%m",
        verbose_name=u"Banner",
        max_length=100)
    url = models.URLField(max_length=200, verbose_name="url")
    index = models.IntegerField(default=100, verbose_name="index")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add time")

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = verbose_name
