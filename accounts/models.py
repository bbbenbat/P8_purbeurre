from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    user_img = models.ImageField(upload_to='images/')
    user_image = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.email