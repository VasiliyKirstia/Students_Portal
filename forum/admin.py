from django.contrib import admin
from forum.models import *

admin.site.register(Topic)
admin.site.register(Answer)
admin.site.register(Author)
admin.site.register(Category)