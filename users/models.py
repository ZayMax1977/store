from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

class User(AbstractUser):
    image = models.ImageField(upload_to ='users_photo',null=True,blank=True)
    gender = models.CharField(max_length=10)
    age = models.PositiveSmallIntegerField(null=True,blank=True)

    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)

