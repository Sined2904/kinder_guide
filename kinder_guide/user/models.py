from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class MyUser(AbstractUser):
    """Кастомная модель юзера."""

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(regex=r'^[\w.@+-]',
                           message='Недопустимые символы в имени пользователя')
        ]
    )
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
        max_length=17,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Номер должен быть набран в формате "+999999999.'
            )
        ]
    )
    child = models.TextField('Имя', max_length=150, blank=True,)

    class Meta:
        ordering = ['-date_joined', ]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
