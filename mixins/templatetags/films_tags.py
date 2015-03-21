from django import template
from films.models import *

register = template.Library()

@register.inclusion_tag('films/partial/categories.html')
def films_categories_partial():
    return {'categories': Category.objects.all()}

