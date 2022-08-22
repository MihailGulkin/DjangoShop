from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    img = models.ImageField(default='no_image.jpg', upload_to='product_image')
    users = models.OneToOneField(User, on_delete=models.CASCADE)
