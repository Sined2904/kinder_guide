<<<<<<< HEAD
# Generated by Django 3.2 on 2023-10-31 13:44
=======
# Generated by Django 4.2.6 on 2023-10-31 13:59
>>>>>>> c687972bc9001a4da1df41f72a862884c3a1b2e2

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0007_school_is_favorited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='is_favorited',
            field=models.BooleanField(default=False, verbose_name='В избранном'),
        ),
    ]
