# Generated by Django 4.2.6 on 2023-10-29 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0012_alter_agecategory_category_alter_school_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='album',
            field=models.ManyToManyField(blank=True, related_name='school', to='education.album', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='school',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='school', to='education.language', verbose_name='Языки'),
        ),
        migrations.AlterField(
            model_name='school',
            name='profile',
            field=models.ManyToManyField(blank=True, related_name='school', to='education.profile', verbose_name='Профиль'),
        ),
        migrations.AlterField(
            model_name='school',
            name='underground',
            field=models.ManyToManyField(blank=True, related_name='school', to='education.underground', verbose_name='Метро'),
        ),
    ]