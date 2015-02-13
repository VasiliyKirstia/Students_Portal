from django import template
from forum.models import Category, Answer, Question

register = template.Library()

@register.inclusion_tag('shared/partial/popular_questions.html')
def popular_topics_partial():
    return {'questions': Question.objects.filter(solved=False).order_by('-answers_count')[:5]}

@register.inclusion_tag('shared/partial/popular_books.html')
def popular_books_partial():
    return {'books': None}

@register.inclusion_tag('shared/partial/popular_films.html')
def popular_films_partial():
    return {'films': None}

@register.inclusion_tag('shared/partial/tag_cloud.html')
def tag_cloud_partial():
    return {'tags': None}