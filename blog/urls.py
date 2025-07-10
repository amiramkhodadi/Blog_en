from django.urls import path, include
from . import views
# app_name = 'blog'
urlpatterns = [
    # path('', views.blog_post, name='blogpost'),
    path('detail/<slug:slug>', views.article_detail, name='article_detail'),
    path('list', views.article_list, name='articles_list'),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('search/', views.search_article, name='search_article'),
]