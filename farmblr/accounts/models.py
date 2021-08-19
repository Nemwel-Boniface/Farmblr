import os
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=25, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    id_number = models.IntegerField()
    country = models.CharField(max_length=150)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username
