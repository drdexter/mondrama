from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug


class Country(models.Model):
    name = models.CharField(max_length=200, verbose_name='Улсын нэр')

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=200, verbose_name='Найруулагчийн нэр')
    picture =models.ImageField(verbose_name='Найруулагч', upload_to='uploads/director')

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=200, verbose_name='Жүжигчний нэр')
    picture =models.ImageField(verbose_name='Найруулагч', upload_to='uploads/director')

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=200, verbose_name='Нэр')
    oname = models.CharField(max_length=200, verbose_name='Өөрийн нэр')
    ryear = models.IntegerField(verbose_name='Гарсан жил')
    picture = models.ImageField(verbose_name='Зургийн нэр', upload_to='uploads/series')
    slug = models.SlugField(max_length=200, unique=True)

    content = models.TextField(verbose_name='Киноны тухай')

    tags = models.ManyToManyField(Tag)
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Eposide(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ангийн нэр')
    link = models.CharField(max_length=200, verbose_name='Х')
    




