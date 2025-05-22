from django.urls import path, include
from . import views
# app_name = 'blog'
urlpatterns = [
    # path('', views.blog_post, name='blogpost'),
    path('detail/<slug:slug>', views.article_detail, name='article_detail'),
    path('list', views.article_list, name='article_list')
]