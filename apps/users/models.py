from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from django.contrib.auth.models import AbstractUser


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
