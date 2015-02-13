from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from tagging_autocomplete.models import TagAutocompleteField
import datetime

YEAR_CHOICES = [(year, year) for year in range(0, datetime.date.today().year + 1)]

class Book(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150, verbose_name='Название')

    author = models.CharField(max_length=50, verbose_name='Автор(ы)')

    imprint_date = models.IntegerField(choices=YEAR_CHOICES, verbose_name='Год издания')

    publisher = models.CharField(max_length=30, verbose_name='Издательство')

    description = RichTextField(verbose_name='Описание')

    book_file = models.FileField(upload_to='books', verbose_name='Книга')

    user = models.ForeignKey(User, related_name='books')

    date = models.DateTimeField(auto_now=True)

    tags = TagAutocompleteField(verbose_name='Тэги',auto_created=True )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = 'Книга'
