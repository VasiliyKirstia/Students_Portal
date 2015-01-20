from django.shortcuts import render
from forum.models import *


def index(request, category_id=None):
    if category_id is not None:
        topics = Topic.objects.filter(category=category_id)
    else:topics = Topic.objects.all()
    return render(request, 'forum/index.html', {'topics': topics})

def detail(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    answers = Answer.objects.filter(topic=topic_id)
    return render(request, 'forum/detail.html', {'topic': topic, 'answers': answers})