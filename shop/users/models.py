from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, RegexValidator
from .service.users.services import validate_size_image


class Profile(models.Model):
    img = models.ImageField(default='no_image_django_shop_py.jpg',
                            upload_to='users_avatar',
                            blank=True,
                            validators=[
                                FileExtensionValidator(
                                    allowed_extensions=['jpg',
                                                        'png']),
                                validate_size_image,
                            ],
                            )
    first_name = models.CharField(max_length=32, help_text='First name',
                                  null=True,
                                  validators=[RegexValidator(
                                      regex=r'^[A-Za-zА-Яа-я]+$')],
                                  )
    last_name = models.CharField(max_length=32, help_text='Last name',
                                 null=True,
                                 validators=[RegexValidator(
                                     regex=r'^[A-Za-zА-Яа-я]+$')],
                                 )
    email = models.EmailField(max_length=64,
                              help_text='Enter a valid email address',
                              unique=True,
                              default='',
                              )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name}'

    # Добавляет проверку на уровне ДБ
    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(
    #             check=~models.Q(first_name=models.F('last_name')),
    #             name='first_and_last_names_different'),
    #     ]
