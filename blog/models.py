from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(**NULLABLE, upload_to='blog/', verbose_name='фото')
    date_published = models.DateField(**NULLABLE, verbose_name='дата публикации')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


