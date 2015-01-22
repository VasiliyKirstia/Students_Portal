from django import template
from forum.models import Category, Answer, Author, Topic

register = template.Library()

@register.inclusion_tag('shared/partial/popular_topics.html')
def popular_topics_partial():
    return {'topics': Topic.objects.filter(solved=False).order_by('-date')[:5]}

@register.inclusion_tag('shared/partial/popular_books.html')
def popular_books_partial():
    return {'books': None}

@register.inclusion_tag('shared/partial/popular_films.html')
def popular_films_partial():
    return {'films': None}

@register.inclusion_tag('shared/partial/tag_cloud.html')
def tag_cloud_partial():
    return {'tags': None}