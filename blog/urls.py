from django.urls import path, include
from . import views
app_name = 'blog'
urlpatterns = [
    # path('', views.blog_post, name='blogpost'),
    path('detail/<int:pk>', views.article_detail, name='artcile_detail')
]