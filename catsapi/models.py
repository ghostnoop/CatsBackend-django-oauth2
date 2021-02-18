from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Cat(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birth = models.DateField(blank=True)
    weight = models.FloatField()
    breed = models.CharField(max_length=100)
    photo = models.ImageField(default="", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
