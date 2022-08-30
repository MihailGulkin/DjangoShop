import datetime

from django.db import models
from users.models import Profile
from django.utils import timezone
from django.core.validators import MaxLengthValidator, MaxValueValidator


class Product(models.Model):
    MOBILE = 'mobile'
    NOTEBOOK = 'notebook'
    PC = 'pc'
    ACC = 'accessories'

    CHOICE_GROUP = {
        (MOBILE, 'mobile'),
        (NOTEBOOK, 'notebook'),
        (PC, 'pc'),
        (ACC, 'accessories'),
    }

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    availability = models.BooleanField()
    group = models.CharField(max_length=20, choices=CHOICE_GROUP,
                             default=MOBILE)
    img = models.ImageField(default='no_image.jpg', upload_to='product_image')

    def __str__(self):
        return f'{self.name}'


class Bucket(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[
        MaxValueValidator(100),
    ])

    def __str__(self):
        return f'{self.owner.user.username} - {self.product.name}'


class CommentReviewAboutProduct(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_pros = models.TextField(max_length=2000, null=True)
    product_cons = models.TextField(max_length=2000, null=True)
    product_comment = models.TextField(max_length=2000, null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.author.user.username} - {self.product.name}'
