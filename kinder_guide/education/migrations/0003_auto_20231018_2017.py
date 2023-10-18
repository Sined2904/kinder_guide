# Generated by Django 3.2 on 2023-10-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20231018_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('image', models.ImageField(upload_to='education/', verbose_name='фото')),
            ],
        ),
        migrations.RemoveField(
            model_name='school',
            name='album',
        ),
        migrations.AddField(
            model_name='school',
            name='album',
            field=models.ManyToManyField(related_name='school', to='education.Album', verbose_name='фото'),
        ),
    ]