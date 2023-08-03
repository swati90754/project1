from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=20,unique=True,null=True,blank=True)
    phone = models.IntegerField(max_length=12,null=True,blank=True)
    gender = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    landmark = models.CharField(max_length=50,null=True,blank=True)
    country = models.CharField(max_length=20,null=True,blank=True)
    state = models.CharField(max_length=20,null=True,blank=True)
    city = models.CharField(max_length=20,null=True,blank=True)
    pincode = models.IntegerField(max_length=6,null=True,blank=True)

    def __str__(self):
        return self.email
