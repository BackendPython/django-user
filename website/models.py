from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin(AbstractUser):
    logo = models.ImageField()

class Files(models.Model):
    file = models.FileField()
    file_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.file_name
