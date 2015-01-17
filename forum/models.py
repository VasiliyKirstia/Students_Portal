from django.db import models


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    text = models.TextField()
    date = models.DateTimeField()
    category = models.ForeignKey(Category)
    author = models.ForeignKey(Author)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    date = models.DateTimeField()
    topic = models.ForeignKey(Topic)
    author = models.ForeignKey(Author)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

