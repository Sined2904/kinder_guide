# Generated by Django 3.2 on 2023-11-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_auto_20231119_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='kindergartens',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kindergartens',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
