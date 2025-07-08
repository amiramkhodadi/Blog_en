from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Article, Category


def article_detail(request , slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request , 'blog/post_details.html',{'article' : article })

def article_list(request ):
    articles = Article.objects.all()
    paginator = Paginator(articles, 1)
    page = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request , 'blog/article_list.html' , {'articles' : page_obj })


def category_detail(request , pk=None):
    category = get_object_or_404(Category, id=pk)
    # print(category.name)
    # articles = category.article_set.all() ==>> az rename shde on bb sorat paiini estefade mikonim chon to model hamono brash rename tarif karde im
    articles = category.articles.all()
    return render(request , 'blog/article_list.html' , {'articles' : articles })