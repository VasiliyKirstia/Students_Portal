from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50,
                            verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        permissions = (
            ('create_questions_category', 'добавлять категории вопросов'),
            ('delete_questions_category', 'удалять категории вопросов'),
            ('change_questions_category', 'редактировать категории вопросов'),
        )


class Question(models.Model):

    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150,
                             verbose_name='заголовок')

    text = RichTextField(verbose_name='описание')

    date = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category,
                                 related_name='questions',
                                 verbose_name='категория')

    user = models.ForeignKey(User,
                             related_name='questions',
                             verbose_name='автор')

    solved = models.BooleanField(default=False,
                                 verbose_name='решено')
    #TODO сделать чтоб оно само увеличивалось при добавлении коментария
    # SOLUTION: добавлять ответы посредством вызова метода класса answer.
    # а в этом методе увеличивать количество ответов у соответствующего вопроса.
    # тогда мы сконцентрируем костыли в одном месте, избавляясь таким образом,
    #  от возможных проблем связаных с последующим сопровождением кода.
    answers_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['solved', '-date']
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
        permissions = (
            ('create_question', 'добавлять вопросы'),
            ('delete_question', 'удалять вопросы'),
            ('change_question', 'редактировать вопросы'),
            ('view_questions', 'просматривать вопросы'),
        )


class Answer(models.Model):

    id = models.AutoField(primary_key=True)

    text = RichTextField()

    date = models.DateTimeField(auto_now=True)

    question = models.ForeignKey(Question,
                                 related_name='questions')

    user = models.ForeignKey(User,
                             related_name='answers')

    def __str__(self):
        return self.text[0:150]

    class Meta:
        ordering = ['date']
        permissions = (
            ('create_answer', 'добавлять ответы'),
            ('delete_answer', 'удалять ответы'),
            ('change_answer', 'редактировать ответы'),
            ('view_answers', 'просматривать ответы'),
        )

