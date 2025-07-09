from django.contrib import admin

from blog.models import Article, Category, Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)