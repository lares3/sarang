from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    phone_number=models.CharField(max_length=12,unique=True)
    is_phone_varified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6)

    USERNAME_FIELD= 'phone_number'
    REQUIRED_FIELDS=[]
    objects=UserManager()
