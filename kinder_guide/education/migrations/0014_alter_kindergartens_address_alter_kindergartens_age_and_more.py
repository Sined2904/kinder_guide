# Generated by Django 4.2.6 on 2023-10-29 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0013_alter_school_album_alter_school_languages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kindergartens',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='age',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='age_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.agecategory', verbose_name='Возрастная категория'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='album',
            field=models.ManyToManyField(blank=True, related_name='kindergartens', to='education.album', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.area', verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='create_dev',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Творческое развитие'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='email',
            field=models.EmailField(blank=True, max_length=250, null=True, verbose_name='Электронный адрес'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='group_suze',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Размер группы'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='intel_dev',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Интеллектуальное развитие'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='kindergartens', to='education.language', verbose_name='Языки'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='music_dev',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Музыкальное развитие'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='price',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Цена в месяц'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='price_of_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Цена в год'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='sport_dev',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Спортивное развитие'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='underground',
            field=models.ManyToManyField(blank=True, related_name='kindergartens', to='education.underground', verbose_name='Метро'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='working_hours',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Время работы'),
        ),
    ]
