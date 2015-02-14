from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import datetime

YEAR_CHOICES = [(year, year) for year in range(1800, datetime.date.today().year + 1)]


class Category(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'


class Film(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150, verbose_name='Название')

    release_date = models.IntegerField(choices=YEAR_CHOICES, verbose_name='Год выхода')

    description = RichTextField(verbose_name='Описание')

    film_file = models.FileField(upload_to='films', verbose_name='Фильм')

    user = models.ForeignKey(User, related_name='films')

    date = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, verbose_name='Категория', related_name='films')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = 'Фильм'