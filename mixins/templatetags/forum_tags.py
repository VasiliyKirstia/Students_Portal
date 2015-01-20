from django import template
from forum.models import Category, Answer, Author, Topic

register = template.Library()

@register.inclusion_tag('forum/partial/categories.html')
def forum_categories_partial():
    return {'categories': Category.objects.all()}

@register.inclusion_tag('forum/partial/archive.html')
def forum_archive_partial():
    return {'months': 0}

@register.inclusion_tag('forum/partial/about_as.html')
def about_as():
    return {}