from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    price = models.FloatField(verbose_name='price')
    image = models.ImageField(verbose_name='image')
    release_date = models.CharField(max_length=50, verbose_name='release_date')
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100)
