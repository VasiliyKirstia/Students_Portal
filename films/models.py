from os.path import join
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import datetime

YEAR_CHOICES = [(year, year) for year in range(datetime.date.today().year, 1799, -1)]

FILMS_FOLDER = 'films'


def UPLOAD_TO(s, fn):
    return join(FILMS_FOLDER, "{hour}{minute}{microsecond}{fn}".format(hour=datetime.datetime.utcnow().hour,
                                                                       minute=datetime.datetime.utcnow().minute,
                                                                       microsecond=datetime.datetime.utcnow().microsecond,
                                                                       fn=fn))


class Category(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Film(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150,
                             verbose_name='название')

    release_date = models.IntegerField(choices=YEAR_CHOICES,
                                       verbose_name='год выхода')

    description = RichTextField(verbose_name='описание')

    film_file = models.FileField(upload_to=UPLOAD_TO,
                                 verbose_name='фильм')

    user = models.ForeignKey(User,
                             related_name='films')

    date = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category,
                                 verbose_name='категория',
                                 related_name='films')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'