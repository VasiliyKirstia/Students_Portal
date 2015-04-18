from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag('chat/chat.html')
def chat():
    return {
        'users': [{'pk': user.pk, 'full_name': "{} {}".format(user.first_name, user.last_name)} for user in User.objects.all()]
    }