from django.db import models
from user.models import MyUser

from colorfield.fields import ColorField


# Абстрактные и общие модели
class Model_For_Additions(models.Model):
    """Абстрактная модель для различных дополнений."""

    name = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Underground(Model_For_Additions):
    """Модель метро."""

    color = ColorField('Цвет ветки',
                       default='#ffffff',
                       null=False)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Метро'
        verbose_name_plural = 'Метро'

    def __str__(self):
        return self.name


class Area(Model_For_Additions):
    """Модель округа."""

    class Meta:
        ordering = ('name', )
        verbose_name = 'Округ'
        verbose_name_plural = 'Округ'

    def __str__(self):
        return self.name


class Language(Model_For_Additions):
    """Модель языков."""

    class Meta:
        ordering = ('name', )
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class Profile(Model_For_Additions):
    """Модель профилей."""

    class Meta:
        ordering = ('name', )
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.name


# Модели школы
class SchoolAlbum(models.Model):
    """Модель альбома изображений для школы."""

    image = models.ImageField(upload_to="school/", verbose_name='фото')
    school = models.ForeignKey(
        'School',
        on_delete=models.CASCADE,
        related_name='album',
        verbose_name='Школа',
        blank=True,
        null=True
    )


class Class(Model_For_Additions):
    """Модель классов для школы."""

    class Meta:
        ordering = ('name', )
        verbose_name = 'Класс в школе'
        verbose_name_plural = 'Классы в школе'

    def __str__(self):
        return self.name


class School(models.Model):
    """Модель школы."""

    name = models.CharField(
        max_length=250,
        null=False,
        verbose_name='Название школы'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    working_hours = models.CharField(
        max_length=250,
        verbose_name='Время работы',
        blank=True,
        null=True
    )
    telephone = models.CharField(
        max_length=250,
        verbose_name='Телефон',
        unique=True
    )
    address = models.CharField(
        max_length=250,
        verbose_name='Адрес',
        blank=True,
        null=True
    )
    email = models.EmailField(
        max_length=250,
        verbose_name='Электронный адрес',
        unique=True,
        blank=True,
        null=True
    )
    website = models.URLField(
        max_length=200,
        verbose_name='Веб-сайт',
        unique=True,
        blank=True,
        null=True
    )
    underground = models.ManyToManyField(
        Underground,
        related_name='school',
        verbose_name='Метро',
        blank=True
    )
    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        verbose_name='Округ',
        blank=True,
        null=True
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена в месяц',
        blank=True,
        null=True
    )
#    age = models.CharField(
#        max_length=250,
#        verbose_name='Возраст',
#        blank=True,
#        null=True
#    )
    price_of_year = models.PositiveIntegerField(
        verbose_name='Цена в год',
        blank=True,
        null=True
    )
    classes = models.ManyToManyField(
        Class,
        related_name='school',
        verbose_name='Классы',
        blank=True
    )
    languages = models.ManyToManyField(
        Language,
        related_name='school',
        verbose_name='Языки',
        blank=True
    )
    profile = models.ManyToManyField(
        Profile,
        related_name='school',
        verbose_name='Профиль',
        blank=True
    )

    class Meta:
        verbose_name = "Школа"
        verbose_name_plural = "Школы"

    def __str__(self):
        return self.name


class Favourites_School(models.Model):
    """Модель Избранного для школы."""

    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favourites_school'
    )
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        verbose_name='Учебное заведение в избранном',
        related_name='favourites_users'
    )

    class Meta:
        verbose_name = 'Избранное - школа'
        verbose_name_plural = 'Избранное - школы'

    def __str__(self):
        return f'Пользователь {self.user} добавил в избранное {self.school}'


# Модели детского сада
class Sport(Model_For_Additions):
    """Модель спортивных занятий (для модели Kindergartens)."""

    class Meta:
        ordering = ('name', )
        verbose_name = 'Спортивное занятие'
        verbose_name_plural = 'Спортивные занятия'

    def __str__(self):
        return self.name


class Create(Model_For_Additions):
    """Модель творческих занятий (для модели Kindergartens)."""

    class Meta:
        ordering = ('name', )
        verbose_name = 'Творческое занятие'
        verbose_name_plural = 'Творческие занятия'

    def __str__(self):
        return self.name


class Intelligence(Model_For_Additions):
    """Модель интеллектуальных занятий (для модели Kindergartens)."""

    class Meta:
        ordering = ('name', )
        verbose_name = 'Интеллектуальное занятие'
        verbose_name_plural = 'Интеллектуальные занятия'

    def __str__(self):
        return self.name


class Music(Model_For_Additions):
    """Модель музыкальных занятий (для модели Kindergartens)."""

    class Meta:
        ordering = ('name', )
        verbose_name = 'Музыкальное занятие'
        verbose_name_plural = 'Музыкальные занятия'

    def __str__(self):
        return self.name


class WorkingHours(Model_For_Additions):
    """Модель времени работы (для модели Kindergartens)."""

    class Meta:
        ordering = ('name', )
        verbose_name = 'Время работы'
        verbose_name_plural = 'Время работы'

    def __str__(self):
        return self.name


class AgeCategory(Model_For_Additions):
    """Модель возрастной категории для сада."""

    class Meta:
        ordering = ('name', )
        verbose_name = 'Возрастная категория'
        verbose_name_plural = 'Возрастные категории'

    def __str__(self):
        return self.name


class KindergartenAlbum(models.Model):
    """Модель альбома изображений для детского сада."""

    image = models.ImageField(upload_to="kindergartens/", verbose_name='фото')
    kindergarten = models.ForeignKey(
        'Kindergartens',
        on_delete=models.CASCADE,
        related_name='album',
        verbose_name='Сад',
        blank=True,
        null=True
    )


class Kindergartens(models.Model):
    """Модель детского сада."""

    name = models.CharField(
        max_length=250,
        null=False,
        verbose_name='Название детского сада'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    telephone = models.CharField(
        max_length=250,
        verbose_name='Телефон',
        unique=True
    )
    address = models.CharField(
        max_length=250,
        verbose_name='Адрес',
        blank=True,
        null=True
    )
    email = models.EmailField(
        max_length=250,
        verbose_name='Электронный адрес',
        unique=True,
        blank=True,
        null=True
    )
    website = models.URLField(
        max_length=200,
        verbose_name='Веб-сайт',
        unique=True,
        blank=True,
        null=True
    )
    underground = models.ManyToManyField(
        Underground,
        related_name='kindergartens',
        verbose_name='Метро',
        blank=True
    )
    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        verbose_name='Округ',
        blank=True,
        null=True
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена в месяц',
        blank=True,
        null=True
    )
#    age = models.CharField(
#        max_length=250,
#        verbose_name='Возраст',
#        blank=True,
#        null=True
#    )
    age_category = models.ManyToManyField(
        AgeCategory,
        verbose_name='Возрастная категория',
        blank=True,
        null=True
    )
    price_of_year = models.PositiveIntegerField(
        verbose_name='Цена в год',
        blank=True,
        null=True
    )
    working_hours = models.ManyToManyField(
        WorkingHours,
        related_name='kindergartens',
        verbose_name='Время работы',
        blank=True
    )
    group_suze = models.CharField(
        max_length=250,
        verbose_name='Размер группы',
        blank=True,
        null=True
    )
    languages = models.ManyToManyField(
        Language,
        related_name='kindergartens',
        verbose_name='Языки',
        blank=True
    )
    sport_dev = models.ManyToManyField(
        Sport,
        related_name='kindergartens',
        verbose_name='Спортивное развитие',
        blank=True
    )
    create_dev = models.ManyToManyField(
        Create,
        related_name='kindergartens',
        verbose_name='Творческое развитие',
        blank=True
    )
    music_dev = models.ManyToManyField(
        Music,
        related_name='kindergartens',
        verbose_name='Музыкальное развитие',
        blank=True
    )
    intel_dev = models.ManyToManyField(
        Intelligence,
        related_name='kindergartens',
        verbose_name='Интеллектуальное развитие',
        blank=True
    )
    preparing_for_school = models.BooleanField(
        'Подготовка к школе',
        default=False
    )

    class Meta:
        verbose_name = "Детский сад"
        verbose_name_plural = "Детские сады"

    def __str__(self):
        return self.name


class Favourites_Kindergartens(models.Model):
    """Модель Избранного для детского сада."""

    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favourites_kindergartens'
    )
    kindergartens = models.ForeignKey(
        Kindergartens,
        on_delete=models.CASCADE,
        verbose_name='Детский садик в избранном',
        related_name='favourites_users'
    )

    class Meta:
        verbose_name = 'Избранное - детский садик'
        verbose_name_plural = 'Избранное - детские сады'

    def __str__(self):
        return (
            f'Пользователь {self.user} '
            f'добавил в избранное {self.kindergartens}'
        )
