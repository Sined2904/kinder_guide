# Generated by Django 4.2.6 on 2023-10-29 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_alter_coursealbum_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Дошкольное обучение', 'Дошкольное обучение'), ('Начальная школа', 'Начальная школа'), ('Основная школа', 'Основная школа'), ('Старшая школа', 'Старшая школа')], max_length=20, verbose_name='Возрастная категория')),
            ],
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
        migrations.AddField(
            model_name='kindergartens',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.profile', verbose_name='Профиль'),
        ),
        migrations.RemoveField(
            model_name='kindergartens',
            name='languages',
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='underground',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.underground', verbose_name='Метро'),
        ),
        migrations.RemoveField(
            model_name='school',
            name='languages',
        ),
        migrations.AlterField(
            model_name='school',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.profile', verbose_name='Профиль'),
        ),
        migrations.AlterField(
            model_name='school',
            name='underground',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.underground', verbose_name='Метро'),
        ),
        migrations.AddField(
            model_name='kindergartens',
            name='age_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.agecategory', verbose_name='Возрастная категория'),
        ),
        migrations.AddField(
            model_name='school',
            name='age_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.agecategory', verbose_name='Возрастная категория'),
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.area', verbose_name='Округ'),
        ),
        migrations.AddField(
            model_name='kindergartens',
            name='languages',
            field=models.ManyToManyField(related_name='kindergartens', to='education.language', verbose_name='Языки'),
        ),
        migrations.AlterField(
            model_name='school',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.area', verbose_name='Округ'),
        ),
        migrations.AddField(
            model_name='school',
            name='languages',
            field=models.ManyToManyField(related_name='school', to='education.language', verbose_name='Языки'),
        ),
    ]