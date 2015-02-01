from django import template
from hallway.models import Developer

register = template.Library()

@register.inclusion_tag('hallway/partial/developers.html')
def developers_partial():
    return {'developers': Developer.objects.all()}