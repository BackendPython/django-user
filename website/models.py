from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin(AbstractUser):
    logo = models.ImageField()
    file = models.FileField()
    file_name = models.CharField(max_length=100)

class Files(models.Model):
    pass