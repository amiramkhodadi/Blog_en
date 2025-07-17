from django.contrib import admin
from django.utils.autoreload import start_django

from blog.models import Article, Category, Comment, Message,Like


class FilterByTitle(admin.SimpleListFilter):
    title = "واژه های پر کابرد"
    parameter_name = "title"

    def lookups(self, request, model_admin):

        return [
            ("python", "پایتون"),
            ("html", "اچ تی ام ال"),
            ("css", "سی اس اس"),

        ]

    def queryset(self, request, queryset):

        if self.value() :
            return queryset.filter(
                title__icontains=self.value()
            )





# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','content' , 'status' , 'author',"show_image"]

             # in feture kheili khobe v miad to on safe y filter sazio ro bar asas model ha bramon anjam mide
    list_filter = ['status',FilterByTitle]
             # ba estefade azin   dar lhze roye list bedon vared shdn b onject mitonim taiqrat ro emal konim
    list_editable = ('author',)
            # in miad y search input dar balaye safe brae ma mizare k khodesh bar asas in feild haye zir toshon search mikone
    search_fields = ['title' , 'content']



admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)

admin.site.register(Like)
