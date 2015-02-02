from django.db import models
from django.contrib.auth.models import User


class Developer(models.Model):

    id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=30,
                                  verbose_name='имя')

    last_name = models.CharField(max_length=30,
                                 verbose_name='фамилия')

    short_description = models.TextField(max_length=80,
                                         verbose_name='краткое описание')

    description = models.TextField(verbose_name='полное описание')

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Разработчик'


class Rules(models.Model):

    id = models.AutoField(primary_key=True)

    text = models.TextField(verbose_name='правила')

    class Meta:
        verbose_name = 'Правила'


class News(models.Model):

    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150,
                             verbose_name='заголовок')

    date = models.DateTimeField()

    description = models.TextField(verbose_name='описание')

    text = models.TextField(verbose_name='новость')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Новости'


class Suggestion(models.Model):

    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User,
                             related_name='suggestions',
                             verbose_name='автор')

    date = models.DateTimeField()

    text = models.TextField(verbose_name='предложение')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Предложения и пожелания'