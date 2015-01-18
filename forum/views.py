from django.shortcuts import render
from forum.models import *


def index(request):
    return render(request, 'forum/index.html', {'title': 'форум'})


def category(request, category_id):
    topics = Topic.objects.filter(category=category_id)
    return render(request, 'forum/category.html', {'topics': topics})
