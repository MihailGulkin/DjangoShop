from django.db import models


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
