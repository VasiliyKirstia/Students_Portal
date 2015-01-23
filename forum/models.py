from django.db import models
from django.contrib.auth.models import User
import datetime


class Category(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Author(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=10)

    #user = models.OneToOneField(User)

    def __str__(self):
        return self.name


class Topic(models.Model):

    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150,
                             verbose_name='Заголовок')

    text = models.TextField(verbose_name='Описание')

    date = models.DateTimeField(default=datetime.datetime.now())

    category = models.ForeignKey(Category,
                                 related_name='topics',
                                 verbose_name='Категория')

    author = models.ForeignKey(Author,
                               related_name='topics',
                               verbose_name='Автор')

    solved = models.BooleanField(default=False,
                                 verbose_name='Решено')

    def __str__(self):
        return self.title


class Answer(models.Model):

    id = models.AutoField(primary_key=True)

    text = models.TextField()

    date = models.DateTimeField(default=datetime.datetime.now())

    topic = models.ForeignKey(Topic, related_name='topics')

    author = models.ForeignKey(Author, related_name='answers')

    def __str__(self):
        return self.text[0:150]


