from django import template

register = template.Library()

@register.inclusion_tag('chat/chat.html')
def chat():
    return None