from django.db import models


class Tag(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(
        Tag,
        through='Scope',
        verbose_name='Тематики статьи',
        related_name='articles'
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    is_main = models.BooleanField(default=False, verbose_name='Основной')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Раздел', related_name='scopes')
