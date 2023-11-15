# Generated by Django 3.2 on 2023-11-15 20:17

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Возрастная категория',
                'verbose_name_plural': 'Возрастные категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Округ',
                'verbose_name_plural': 'Округ',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Класс в школе',
                'verbose_name_plural': 'Классы в школе',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Favourites_Kindergartens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранное - детский садик',
                'verbose_name_plural': 'Избранное - детские сады',
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='GroupSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Размер группы',
                'verbose_name_plural': 'Размеры групп',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('kindergarten', 'kindergartens'), ('school', 'schools')], default='school', max_length=13)),
                ('name', models.CharField(max_length=250, verbose_name='Название школы')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('working_hours', models.CharField(blank=True, max_length=250, null=True, verbose_name='Время работы')),
                ('telephone', models.CharField(max_length=250, unique=True, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Адрес')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, unique=True, verbose_name='Электронный адрес')),
                ('website', models.URLField(blank=True, null=True, unique=True, verbose_name='Веб-сайт')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена в месяц')),
                ('price_of_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена в год')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.area', verbose_name='Округ')),
                ('classes', models.ManyToManyField(blank=True, related_name='school', to='education.Class', verbose_name='Классы')),
                ('languages', models.ManyToManyField(blank=True, related_name='school', to='education.Language', verbose_name='Языки')),
                ('profile', models.ManyToManyField(blank=True, related_name='school', to='education.Profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Underground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('color', colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=18, samples=None, verbose_name='Цвет ветки')),
            ],
            options={
                'verbose_name': 'Метро',
                'verbose_name_plural': 'Метро',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Время работы',
                'verbose_name_plural': 'Время работы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SchoolAverageRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_rating', models.FloatField(blank=True, default=None, null=True, verbose_name='Средняя оценка')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.school')),
            ],
            options={
                'verbose_name': 'Средняя оценка школы',
                'verbose_name_plural': 'Средние оценки школ',
            },
        ),
        migrations.CreateModel(
            name='SchoolAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='school/', verbose_name='фото')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='education.school', verbose_name='Школа')),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='underground',
            field=models.ManyToManyField(blank=True, related_name='school', to='education.Underground', verbose_name='Метро'),
        ),
        migrations.CreateModel(
            name='Kindergartens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('kindergarten', 'kindergartens'), ('school', 'schools')], default='kindergarten', max_length=13)),
                ('name', models.CharField(max_length=250, verbose_name='Название детского сада')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('telephone', models.CharField(max_length=250, unique=True, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Адрес')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, unique=True, verbose_name='Электронный адрес')),
                ('website', models.URLField(blank=True, null=True, unique=True, verbose_name='Веб-сайт')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена в месяц')),
                ('price_of_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена в год')),
                ('create_dev', models.CharField(blank=True, max_length=250, null=True, verbose_name='Творческое развитие')),
                ('intel_dev', models.CharField(blank=True, max_length=250, null=True, verbose_name='Интеллектуальное развитие')),
                ('music_dev', models.CharField(blank=True, max_length=250, null=True, verbose_name='Музыкальное развитие')),
                ('sport_dev', models.CharField(blank=True, max_length=250, null=True, verbose_name='Спортивное развитие')),
                ('preparing_for_school', models.BooleanField(default=False, verbose_name='Подготовка к школе')),
                ('age_category', models.ManyToManyField(blank=True, to='education.AgeCategory', verbose_name='Возрастная категория')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.area', verbose_name='Округ')),
                ('group_size', models.ManyToManyField(blank=True, related_name='kindergartens', to='education.GroupSize', verbose_name='Размер группы')),
                ('languages', models.ManyToManyField(blank=True, related_name='kindergartens', to='education.Language', verbose_name='Языки')),
                ('underground', models.ManyToManyField(blank=True, related_name='kindergartens', to='education.Underground', verbose_name='Метро')),
                ('working_hours', models.ManyToManyField(blank=True, related_name='kindergartens', to='education.WorkingHours', verbose_name='Время работы')),
            ],
            options={
                'verbose_name': 'Детский сад',
                'verbose_name_plural': 'Детские сады',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='KindergartenAverageRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_rating', models.FloatField(blank=True, default=None, null=True, verbose_name='Средняя оценка')),
                ('kindergarten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.kindergartens')),
            ],
            options={
                'verbose_name': 'Средняя оценка детского сада',
                'verbose_name_plural': 'Средние оценки детских садов',
            },
        ),
        migrations.CreateModel(
            name='KindergartenAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='kindergartens/', verbose_name='фото')),
                ('kindergarten', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='education.kindergartens', verbose_name='Сад')),
            ],
        ),
        migrations.CreateModel(
            name='Favourites_School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_users', to='education.school', verbose_name='Учебное заведение в избранном')),
            ],
            options={
                'verbose_name': 'Избранное - школа',
                'verbose_name_plural': 'Избранное - школы',
                'ordering': ('user',),
            },
        ),
    ]
