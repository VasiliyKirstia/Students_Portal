from django.shortcuts import get_object_or_404, redirect, render

def error_page_404(request):
    return render(request, 'shared/404.html', {})

def error_page_500(request):
    return render(request, 'shared/500.html', {})