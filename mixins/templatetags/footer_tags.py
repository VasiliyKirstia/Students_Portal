from django import template
from forum.models import Question
from library.models import Book
from films.models import Film

register = template.Library()

@register.inclusion_tag('shared/partial/popular_questions.html')
def popular_topics_partial():
    return {'questions': Question.objects.filter(solved=False).order_by('-answers_count')[:5]}

@register.inclusion_tag('shared/partial/resent_books.html')
def popular_books_partial():
    return {'books': Book.objects.all()[:5]}

@register.inclusion_tag('shared/partial/resent_films.html')
def popular_films_partial():
    return {'films': Film.objects.all()[:5]}