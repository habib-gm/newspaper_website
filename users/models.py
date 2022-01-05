from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null = True, blank=True)
    image = models.ImageField(null = True, blank=True, upload_to = "images/")
    