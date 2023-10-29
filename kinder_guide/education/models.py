from django.db import models
from user.models import MyUser

#Абстрактные и общие модели
class Model_For_Additions(models.Model):
    """Абстрактная модель для различных дополнений."""
    name = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')

    class Meta:
        abstract = True

class Underground(Model_For_Additions):
    """Модель метро."""

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


class Album(models.Model):
    """Модель для фото."""
    name = models.CharField(max_length=256, verbose_name='Название')
    image = models.ImageField(upload_to="education/", verbose_name='фото')

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


class AgeCategory(models.Model):
    """Модель возрастной категории."""
    CATEGORY_CHOICES = (
        ('Дошкольное обучение', 'Дошкольное обучение'),
        ('Начальная школа', 'Начальная школа'),
        ('Основная школа', 'Основная школа'),
        ('Старшая школа', 'Старшая школа'),
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name='Возрастная категория',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.category


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
    album = models.ManyToManyField(
        Album,
        related_name='school',
        verbose_name='фото',
        blank=True
    )
    working_hours = models.CharField(
        max_length=250,
        verbose_name='Время работы',
        blank=True,
        null=True
    )
    telephone = models.CharField(
        max_length=250,
        verbose_name='Телефон'
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
        on_delete=models.SET_NULL,
        verbose_name='Округ',
        blank=True,
        null=True
    )
    price = models.PositiveSmallIntegerField(
        verbose_name='Цена в месяц',
        blank=True,
        null=True
    )
    age = models.CharField(
        max_length=250,
        verbose_name='Возраст',
        blank=True,
        null=True
    )
    age_category = models.ForeignKey(
        AgeCategory,
        on_delete=models.SET_NULL,
        verbose_name='Возрастная категория',
        blank=True,
        null=True
    )
    price_of_year = models.PositiveSmallIntegerField(
        verbose_name='Цена в год',
        blank=True,
        null=True
    )
    classes = models.CharField(
        max_length=250,
        verbose_name='Классы',
        blank=True,
        null=True
    )
    name_author = models.CharField(
        max_length=250,
        verbose_name='Имя автора',
        blank=True,
        null=True
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
    """Модель Избранного для школы"""
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


#Модели про детский сад
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


class Kindergartens(models.Model):
    """Модель детского сада."""
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
    album =  models.ManyToManyField(
        Album,
        related_name='kindergartens',
        verbose_name='фото',
        blank=True
    )
    telephone = models.CharField(
        max_length=250,
        verbose_name='Телефон'
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
        on_delete=models.SET_NULL,
        verbose_name='Округ',
        blank=True,
        null=True
    )
    price = models.PositiveSmallIntegerField(
        verbose_name='Цена в месяц',
        blank=True,
        null=True
    )
    age = models.CharField(
        max_length=250,
        verbose_name='Возраст',
        blank=True,
        null=True
    )
    age_category = models.ForeignKey(
        AgeCategory,
        on_delete=models.SET_NULL,
        verbose_name='Возрастная категория',
        blank=True,
        null=True
    )
    price_of_year = models.PositiveSmallIntegerField(
        verbose_name='Цена в год',
        blank=True,
        null=True
    )
    working_hours = models.CharField(
        max_length=250,
        verbose_name='Время работы',
        blank=True,
        null=True
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
    sport_dev = models.CharField(
        max_length=250,
        verbose_name='Спортивное развитие',
        blank=True,
        null=True
    )
    '''
    models.ManyToManyField(
        Sport,
        related_name='kindergartens', 
        verbose_name='Спортивное развитие'
    )
    '''
    create_dev = models.CharField(
        max_length=250,
        verbose_name='Творческое развитие',
        blank=True,
        null=True
    )
    '''
    models.ManyToManyField(
        Create,
        related_name='kindergartens', 
        verbose_name='Творческое развитие'
    )
    '''
    music_dev = models.CharField(
        max_length=250,
        verbose_name='Музыкальное развитие',
        blank=True,
        null=True
    )
    '''
    models.ManyToManyField(
        Music,
        related_name='kindergartens', 
        verbose_name='Музыкальное развитие'
    )
    '''
    intel_dev = models.CharField(
        max_length=250,
        verbose_name='Интеллектуальное развитие',
        blank=True,
        null=True
    )
    '''
    models.ManyToManyField(
        Intelligence,
        related_name='kindergartens', 
        verbose_name='Интеллектуальное развитие'
    )
    '''
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
        return f'Пользователь {self.user} добавил в избранное {self.kindergartens}'


#Модели про курсы
class CourseAlbum(models.Model):
    """Модель альбома изображений для курсов."""
    name = models.CharField(max_length=256, verbose_name='Название')
    image = models.ImageField(upload_to="course/", verbose_name='фото')
    course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name='album',
        verbose_name='Курсы',
        null=True
    )

    def __str__(self):
        return self.name
    

class Course(models.Model):
    """Модель курса."""
    name = models.CharField(
            max_length=250,
            null=False,
            verbose_name='Название курсов'
        )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    telephone = models.CharField(max_length=250, verbose_name='Телефон')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    email = models.EmailField(max_length=250, verbose_name='Электронный адрес')
    underground = models.CharField(max_length=250, verbose_name='Метро')
    '''
    models.ManyToManyField(
        Underground,
        related_name='course',
        verbose_name='Метро'
    )
    '''
    area = models.CharField(max_length=250, verbose_name='Округ')
    price = models.PositiveSmallIntegerField(verbose_name='Цена в месяц')
    age = models.CharField(max_length=250, verbose_name='Возраст')
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Favourites_Course(models.Model):
    """Модель Избранного для курсов."""
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favourites_course'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс в избранном',
        related_name='favourites_users'
    )

    class Meta:
        verbose_name = 'Избранное - курс'
        verbose_name_plural = 'Избранное - курсы'

    def __str__(self):
        return f'Пользователь {self.user} добавил в избранное {self.course}'