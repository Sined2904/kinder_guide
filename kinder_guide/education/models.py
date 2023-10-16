from django.db import models
from user.models import MyUser
from phonenumber_field.modelfields import PhoneNumberField

class Language(models.Model):
    """Модель языков (для модели School)."""
    name = models.CharField(max_length=256, verbose_name='Название языка')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')

    class Meta:
        ordering = ('name', )
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class Profile(models.Model):
    """Модель профилей (для модели School)."""
    name = models.CharField(max_length=256, verbose_name='Название профиля')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')
    #возможно нужно будет добавить разные предметы из которых состоит профиль

    class Meta:
        ordering = ('name', )
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.name


class School(models.Model):
    """Модель школы."""
    name = models.CharField(
        max_length=250,
        null=False,
        verbose_name='Название школы'
    )
    album = models.ImageField(
        upload_to="education/",
        verbose_name="Изображение",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    telephone = PhoneNumberField(blank=True, region='RU')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    price = models.PositiveSmallIntegerField(verbose_name='Цена в месяц')
    price_of_year = models.PositiveSmallIntegerField(verbose_name='Цена в год')
    email = models.EmailField(max_length=250, verbose_name='Электронный адрес')
    age = models.CharField(max_length=250, verbose_name='Возраст')
    classes = models.CharField(max_length=250, verbose_name='Классы')
    name_author = models.CharField(max_length=250, verbose_name='Имя автора')
    underground = models.CharField(max_length=250, verbose_name='Метро')
    area = models.CharField(max_length=250, verbose_name='Округ')
    languages = models.ManyToManyField(
        Language,
        related_name='school', 
        verbose_name='Языки'
    )
    profile = models.ManyToManyField(
        Profile,
        related_name='school', 
        verbose_name='Профиль'
    )

    class Meta:
        verbose_name = "Школа"
        verbose_name_plural = "Школы"

    def __str__(self):
        return self.name


class Favourites_school(models.Model):
    """Модель Избранного для школы"""
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favourites_education'
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
        return f'Пользователь {self.user} добавил в избранное {self.education}'


'''
class Lesson(models.Model):
    """Модель уроков (для модели Specialist)."""
    name = models.CharField(max_length=256, verbose_name='Название урока')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name


class Educational_form(models.Model):
    """Модель форм обучения (для модели Specialist)."""
    name = models.CharField(max_length=256, verbose_name='Форма обучения')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Форма обучения'
        verbose_name_plural = 'Формы обучения'

    def __str__(self):
        return self.name


class Achievement(models.Model):
    """Модель достижений (для модели Specialist)."""
    name = models.CharField(max_length=256, verbose_name='Достижения')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.name


class Specialist(models.Model):
    """Модель специалиста."""
    ROLE_CHOICES = (
        ('Репетитор', 'Репетитор'),
        ('Психолог', 'Психолог'),
    )
    role = models.CharField(
        max_length=25, choices=ROLE_CHOICES, default=None,
        verbose_name='Выберите тип'
    )
    image = models.ImageField(
        upload_to="specialist/",
        verbose_name="Изображение",
    )    
    first_name = models.CharField(max_length=25, verbose_name='Имя')
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=25, verbose_name='Отчество')
    experience = models.PositiveSmallIntegerField(verbose_name='Стаж работы(лет)')
    lessons = models.ManyToManyField(
        Lesson,
        related_name='specialist', 
        verbose_name='Уроки'
    )
    educational_form = models.ManyToManyField(
        Educational_form,
        related_name='specialist', 
        verbose_name='Форма обучения'
    )
    #Округ(а)
    price_min = models.PositiveSmallIntegerField(verbose_name='от')
    price_max = models.PositiveSmallIntegerField(verbose_name='до')
    #добавить расписание
    #Образование (в форме таблицы + прирепленные фото дипломов)
    achievement = models.ForeignKey(
        Achievement,
        null=True,
        on_delete=models.SET_NULL,
        related_name='specialist',
        verbose_name='Достижения',
    )


    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

    def __str__(self):
        return f'{self.last_name}{self.first_name}{self.patronymic}'


class Favourites_specialist(models.Model):
    """Модель Избранного для спациалиста"""
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favourites_specialist'
    )
    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE,
        verbose_name='Специалист в избранном',
        related_name='favourites_users'
    )

    class Meta:
        verbose_name = 'Избранное - специалисты'
        verbose_name_plural = 'Избранное - специалисты'

    def __str__(self):
        return f'Пользователь {self.user} добавил в избранное {self.specialist}'
'''