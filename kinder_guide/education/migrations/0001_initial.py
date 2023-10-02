# Generated by Django 3.2 on 2023-10-02 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Достижения')),
                ('slug', models.SlugField(unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название образовательного учрждения')),
                ('role', models.CharField(choices=[('Школа', 'Школа'), ('Сад', 'Сад'), ('Курс', 'Курс')], default=None, max_length=25, verbose_name='Выберите тип')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('telephone', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('price', models.PositiveSmallIntegerField(verbose_name='Цена')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Учебное заведение',
                'verbose_name_plural': 'Учебные заведения',
            },
        ),
        migrations.CreateModel(
            name='Educational_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Форма обучения')),
                ('slug', models.SlugField(unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Форма обучения',
                'verbose_name_plural': 'Формы обучения',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название языка')),
                ('slug', models.SlugField(unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название урока')),
                ('slug', models.SlugField(unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название языка')),
                ('slug', models.SlugField(unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Репетитор', 'Репетитор'), ('Психолог', 'Психолог')], default=None, max_length=25, verbose_name='Выберите тип')),
                ('image', models.ImageField(upload_to='specialist/', verbose_name='Изображение')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=25, verbose_name='Отчество')),
                ('experience', models.PositiveSmallIntegerField(verbose_name='Стаж работы(лет)')),
                ('price_min', models.PositiveSmallIntegerField(verbose_name='от')),
                ('price_max', models.PositiveSmallIntegerField(verbose_name='до')),
                ('achievement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialist', to='education.achievement', verbose_name='Достижения')),
                ('educational_form', models.ManyToManyField(related_name='specialist', to='education.Educational_form', verbose_name='Форма обучения')),
                ('lessons', models.ManyToManyField(related_name='specialist', to='education.Lesson', verbose_name='Уроки')),
            ],
            options={
                'verbose_name': 'Специалист',
                'verbose_name_plural': 'Специалисты',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='education/')),
                ('default', models.BooleanField(default=False)),
                ('width', models.FloatField(default=100)),
                ('length', models.FloatField(default=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='education.imagealbum')),
            ],
        ),
        migrations.CreateModel(
            name='Favourites_specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_users', to='education.specialist', verbose_name='Специалист в избранном')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_specialist', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Избранное - специалисты',
                'verbose_name_plural': 'Избранное - специалисты',
            },
        ),
        migrations.CreateModel(
            name='Favourites_education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_users', to='education.education', verbose_name='Учебное заведение в избранном')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_education', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Избранное - учебные учреждения',
                'verbose_name_plural': 'Избранное - учебные учреждения',
            },
        ),
        migrations.AddField(
            model_name='education',
            name='album',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='education.imagealbum'),
        ),
        migrations.AddField(
            model_name='education',
            name='languages',
            field=models.ManyToManyField(related_name='education', to='education.Language', verbose_name='Языки'),
        ),
        migrations.AddField(
            model_name='education',
            name='profile',
            field=models.ManyToManyField(related_name='education', to='education.Profile', verbose_name='Профиль'),
        ),
    ]
