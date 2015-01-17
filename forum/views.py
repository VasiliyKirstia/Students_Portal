from django.shortcuts import render
from forum.models import *


def index(request):
    return render(request, 'forum/index.html', {'title': 'форум'})


def category(request):
    topics = Topic.objects.filter(category=request.category_id)
    return render(request, 'forum/category.html', {'topics': topics})
