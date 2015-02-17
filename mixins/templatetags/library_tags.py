from django import template
from library.models import *

register = template.Library()

@register.inclusion_tag('library/partial/categories.html')
def library_tags_partial():
    return {'categories': Category.objects.all()}

