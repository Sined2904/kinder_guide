# Generated by Django 3.2 on 2023-11-15 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0001_initial'),
        ('comments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewschool',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewschool',
            name='review_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='education.school'),
        ),
        migrations.AddField(
            model_name='reviewkindergarten',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewkindergarten',
            name='review_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='education.kindergartens'),
        ),
        migrations.AddConstraint(
            model_name='reviewschool',
            constraint=models.UniqueConstraint(fields=('author', 'review_post'), name='unique_author_reviewschool'),
        ),
        migrations.AddConstraint(
            model_name='reviewkindergarten',
            constraint=models.UniqueConstraint(fields=('author', 'review_post'), name='unique_author_reviewkindergarten'),
        ),
    ]
