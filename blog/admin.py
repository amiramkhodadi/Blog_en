from django.contrib import admin

from blog.models import Article, Category

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)