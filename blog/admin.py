from django.contrib import admin
from django.utils.autoreload import start_django

from blog.models import Article, Category, Comment, Message

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)