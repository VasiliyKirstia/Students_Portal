from django.db import models


#class Author:
#    id = models.AutoField(primary_key=True)
#    name = models.CharField("имя автора", max_length=50)
#    questions = models.ForeignKey(Question, verbose_name="все вопросы автора")
#    comments = models.ForeignKey(Comment, verbose_name="все ответы автора")
#
#
#class Question:
#    id = models.AutoField(primary_key=True)
#    question = models.CharField("вопрос",max_length=150)
#    detail = models.TextField("дополнительное описание вопроса")
#    create_date = models.DateTimeField("время создания вопроса")
#    comments = models.ForeignKey(Comment, verbose_name="все коментарии к вопросу")
#
#class Comment:
#    id = models.AutoField(primary_key=True)
#    text = models.TextField("текст ответа")
#    create_date = models.DateTimeField("дата создания")
