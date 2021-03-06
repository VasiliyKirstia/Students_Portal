from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Developer(models.Model):

    id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=30,
                                  verbose_name='имя')

    last_name = models.CharField(max_length=30,
                                 verbose_name='фамилия')

    short_description = models.TextField(max_length=80,
                                         verbose_name='краткое описание')

    description = RichTextField(verbose_name='полное описание')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['first_name']
        verbose_name = 'разработчик'
        verbose_name_plural = 'разработчики'


class Rules(models.Model):

    id = models.AutoField(primary_key=True)

    text = models.TextField(verbose_name='правила')

    def __str__(self):
        return 'список правил № '+ str(self.id)

    class Meta:
        verbose_name = 'правила'
        verbose_name_plural = 'правила'


class News(models.Model):

    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150,
                             verbose_name='заголовок')

    date = models.DateTimeField(auto_now=True)

    description = models.TextField(verbose_name='описание')

    text = RichTextField(verbose_name='новость')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


class Suggestion(models.Model):

    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User,
                             related_name='suggestions',
                             verbose_name='автор')

    date = models.DateTimeField(auto_now=True)

    text = RichTextField(verbose_name='предложение', )

    def __str__(self):
        return self.text[:150]

    class Meta:
        ordering = ['-date']
        verbose_name = 'пожелание (предложение)'
        verbose_name_plural = 'предложения (пожелания)'