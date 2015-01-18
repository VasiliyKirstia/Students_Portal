from django.shortcuts import render
from forum.models import *

def make_category_list():
    category_list=[]
    for cat in Category.objects.all():
        category_list.append({'category': cat,'topics_count': Topic.objects.filter(category_id=cat.id)})
    return category_list

def index(request, category_id=None):
    category_list = make_category_list()
    if category_id is not None:
        topics = Topic.objects.filter(category=category_id)
    else:topics = Topic.objects.all()
    return render(request, 'forum/index.html', {'topics': topics, 'category_list': category_list})

def detail(request, topic_id):
    category_list = make_category_list()
    topic = Topic.objects.filter(id=topic_id)
    answers = Answer.objects.filter(topic=topic_id)
    return render(request, 'forum/detail.html', {'topic': topic, 'answers': answers, 'category_list': category_list})