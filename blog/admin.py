from django.contrib import admin
from django.utils.autoreload import start_django

from blog.models import Article, Category, Comment, Message

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title' , 'status' , 'author']

             # in feture kheili khobe v miad to on safe y filter sazio ro bar asas model ha bramon anjam mide
    list_filter = ['status']
             # ba estefade azin   dar lhze roye list bedon vared shdn b onject mitonim taiqrat ro emal konim
    list_editable = ('author',)



admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)

