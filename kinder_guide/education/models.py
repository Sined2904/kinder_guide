from django.db import models
from user.models import MyUser

#Абстрактные модели
class Model_For_Additions(models.Model):
    """Абстрактная модель для различных дополнений."""
    name = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')

    class Meta:
        abstract = True


class Education(models.Model):
    """Абстрактная модель для учебных заведений."""
    name = models.CharField(
            max_length=250,
            null=False,
            verbose_name='Название школы'
        )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    album = models.ImageField(
        upload_to="education/",
        verbose_name="Изображение",
    )
    telephone = models.CharField(max_length=250, verbose_name='Телефон')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    email = models.EmailField(max_length=250, verbose_name='Электронный адрес')
    underground = models.CharField(max_length=250, verbose_name='Метро')
    area = models.CharField(max_length=250, verbose_name='Округ')
    price = models.PositiveSmallIntegerField(verbose_name='Цена в месяц')
    age = models.CharField(max_length=250, verbose_name='Возраст')

    class Meta:
        abstract = True


#Модели про школу
class Language(Model_For_Additions):
    """Модель языков (для модели School)."""
    class Meta:
        ordering = ('name', )
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class Profile(Model_For_Additions):
    """Модель профилей (для модели School)."""
    class Meta:
        ordering = ('name', )
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.name


class School(Education):
    """Модель школы."""
    price_of_year = models.PositiveSmallIntegerField(verbose_name='Цена в год')
    classes = models.CharField(max_length=250, verbose_name='Классы')
    name_author = models.CharField(max_length=250, verbose_name='Имя автора')
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


class Kindergartens(Education):
    """Модель детского сада."""
    price_of_year = models.PositiveSmallIntegerField(verbose_name='Цена в год')
    working_hours = models.CharField(max_length=250, verbose_name='Время работы')
    group_suze = models.CharField(max_length=250, verbose_name='Размер группы')
    languages = models.ManyToManyField(
        Language,
        related_name='kindergartens', 
        verbose_name='Иностранные языки'
    )
    sport_dev = models.ManyToManyField(
        Sport,
        related_name='kindergartens', 
        verbose_name='Спортивное развитие'
    )
    create_dev = models.ManyToManyField(
        Create,
        related_name='kindergartens', 
        verbose_name='Творческое развитие'
    )
    music_dev = models.ManyToManyField(
        Music,
        related_name='kindergartens', 
        verbose_name='Музыкальное развитие'
    )
    intel_dev = models.ManyToManyField(
        Intelligence,
        related_name='kindergartens', 
        verbose_name='Интеллектуальное развитие'
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
        return f'Пользователь {self.user} добавил в избранное {self.kindergartens}'


#Модели про курсы
class Course(Education):
    """Модель курса."""
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
