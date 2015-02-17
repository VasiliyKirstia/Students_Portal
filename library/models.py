from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import datetime

YEAR_CHOICES = [(year, year) for year in range(datetime.date.today().year, 1499, -1)]


class Tag(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Book(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150,
                             verbose_name='название')

    author = models.CharField(max_length=50,
                              verbose_name='автор(ы)')

    imprint_date = models.IntegerField(choices=YEAR_CHOICES,
                                       verbose_name='год издания')

    publisher = models.CharField(max_length=30,
                                 verbose_name='издательство')

    description = RichTextField(verbose_name='описание')

    book_file = models.FileField(upload_to='books',
                                 verbose_name='книга')

    user = models.ForeignKey(User,
                             related_name='books')

    date = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag,
                                  verbose_name='теги',
                                  related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
