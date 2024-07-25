from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password, check_password
from django.db import models

class CustomUser(AbstractBaseUser):
    phone = models.CharField(max_length=13, unique=True)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=128)  # Adjust max_length to fit hashed password length

    USERNAME_FIELD = 'phone'

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
