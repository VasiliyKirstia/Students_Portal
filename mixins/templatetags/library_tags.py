from django import template
from library.models import *

register = template.Library()

@register.inclusion_tag('library/partial/tags.html')
def library_tags_partial():
    return {'tags': Tag.objects.all()}

