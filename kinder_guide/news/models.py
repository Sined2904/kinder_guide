from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    content = models.TextField(verbose_name='Контент')
    date_posted = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    image = models.ImageField(upload_to="news/", verbose_name='Картинка')

    class Meta:        
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-date_posted']

    def __str__(self):
        return self.title
