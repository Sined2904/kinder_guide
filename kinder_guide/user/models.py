from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from .managers import MyUserManager


class MyUser(AbstractUser):
    """Кастомная модель юзера."""

    username = models.TextField('Username', blank=True, max_length=150,)
    password = models.CharField(
        'Пароль',
        max_length=150,
    )
    email = models.EmailField(
        'e-mail',
        max_length=254,
        unique=True,
    )
    first_name = models.TextField('Имя', max_length=150,)
    last_name = models.TextField('Фамилия', max_length=150,)
    phone = models.CharField(
        'Номер телефона',
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                # regex=r'^\+?1?\d{9,15}$',
                # message='Номер должен быть набран в формате "+999999999".'
                regex=r'^\+\d{1,3}[\d()-]{6,14}\d$',
                message='Номер должен быть набран в формате "+9(9)9999999".'
            )
        ]
    )
    # child = models.TextField('Имя', max_length=150, blank=True,)
    child_first_name = models.TextField('Имя ребенка',
                                        max_length=150,
                                        blank=True,)
    child_last_name = models.TextField('Фамилия ребенка',
                                       max_length=150,
                                       blank=True,)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]

    class Meta:
        ordering = ['-date_joined', ]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
