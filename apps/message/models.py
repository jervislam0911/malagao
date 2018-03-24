from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class UserMessage(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="First name")
    last_name = models.CharField(max_length=20, verbose_name="Last name")
    email = models.EmailField(verbose_name="Email")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    message = models.CharField(max_length=500, verbose_name="message")
    object_id = models.CharField(primary_key=True, verbose_name="primary_key", max_length=50, default="")

    class Meta:
        verbose_name = "User message"
        # db_table = "user_meassage"
        # ordering = '-object_id'
        verbose_name_plural = verbose_name

