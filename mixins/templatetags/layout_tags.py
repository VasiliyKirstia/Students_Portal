from django import template
from forum.models import Category, Answer, Author, Topic

register = template.Library()

@register.inclusion_tag('shared/partial/popular_topics.html')
def forum_categories_partial():
    return {'categories': Topic.objects.order_by()}
