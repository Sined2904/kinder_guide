# Generated by Django 3.2 on 2023-10-29 15:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(message='Номер должен быть в формате "+9(999)999-99-99".', regex='^\\+\\d{1,3}[\\d()-]{6,14}\\d$')], verbose_name='Номер телефона'),
        ),
    ]