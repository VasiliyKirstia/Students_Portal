from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50,
                            verbose_name='Название')

    def __str__(self):
        return self.name


class Topic(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150,
                             verbose_name='Заголовок')

    text = models.TextField(verbose_name='Описание')

    date = models.DateTimeField()

    category = models.ForeignKey(Category,
                                 related_name='topics',
                                 verbose_name='Категория')

    user = models.ForeignKey(User,
                             related_name='topics',
                             verbose_name='Автор')

    solved = models.BooleanField(default=False,
                                 verbose_name='Решено')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['solved', '-date']


class Answer(models.Model):
    id = models.AutoField(primary_key=True)

    text = models.TextField()

    date = models.DateTimeField()

    topic = models.ForeignKey(Topic, related_name='topics')

    user = models.ForeignKey(User, related_name='answers')

    def __str__(self):
        return self.text[0:150]

    class Meta:
        ordering = ['date']

