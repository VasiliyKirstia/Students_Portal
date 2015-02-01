from django.db import models

class Developer(models.Model):

    id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=30,
                                  verbose_name='имя')

    last_name = models.CharField(max_length=30,
                                 verbose_name='фамилия')

    short_description = models.TextField(max_length=80,
                                         verbose_name='короткое описание')

    description = models.TextField(verbose_name='полное описание')

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Разработчик'


class Rules(models.Model):
    id=models.AutoField(primary_key=True)

    text=models.TextField(verbose_name='правила')

    class Meta:
        verbose_name = 'Правила'