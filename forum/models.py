from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50,
                            verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'


class Question(models.Model):

    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150,
                             verbose_name='Заголовок')

    text = RichTextField(verbose_name='Описание')

    date = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category,
                                 related_name='questions',
                                 verbose_name='Категория')

    user = models.ForeignKey(User,
                             related_name='questions',
                             verbose_name='Автор')

    solved = models.BooleanField(default=False,
                                 verbose_name='Решено')
    #TODO сделать чтоб оно само увеличивалось при добавлении коментария
    answers_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['solved', '-date']
        verbose_name = 'Вопрос'


class Answer(models.Model):

    id = models.AutoField(primary_key=True)

    text = RichTextField()

    date = models.DateTimeField(auto_now=True)

    question = models.ForeignKey(Question, related_name='questions')

    user = models.ForeignKey(User, related_name='answers')

    def __str__(self):
        return self.text[0:150]

    class Meta:
        ordering = ['date']

