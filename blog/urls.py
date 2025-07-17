from django.urls import path, include
from . import views
# app_name = 'blog'
urlpatterns = [
    # path('', views.blog_post, name='blogpost'),
    path('article/detail/<slug:slug>', views.article_detail, name='article_detail'),
    path('article/list', views.article_list, name='articles_list'),
    path('article/category/<int:pk>', views.category_detail, name='category_detail'),
    path('article/search/', views.search_article, name='search_article'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('article/like/<slug:slug>/<int:pk>', views.like, name='like'),
]

# tamrin :

# path('article/list', views.ArticleListView.as_view(), name='articles_list'),
# path('article/list', views.ArticleListTemplateView.as_view(), name='articles_list'),