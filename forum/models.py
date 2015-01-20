from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField()
    category = models.ForeignKey(Category, related_name='topics')
    author = models.ForeignKey(Author, related_name='topics')

    def __str__(self):
        return self.title


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    date = models.DateTimeField()
    topic = models.ForeignKey(Topic, related_name='answers')
    author = models.ForeignKey(Author, related_name='answers')

    def __str__(self):
        return self.text[0:150]


