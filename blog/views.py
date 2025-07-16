from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.views.generic import TemplateView, RedirectView

from blog.models import Article, Category, Comment, Message
from blog.forms import  MassageForm


def article_detail(request , slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        comment_id = request.POST.get('comment_id')
        content = request.POST.get('content')
        Comment.objects.create(content=content, article=article, author=request.user, parent_id =comment_id)
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


def search_article(request):
    q = request.GET.get("q")
    articles = Article.objects.filter(title__icontains=q)
    paginator = Paginator(articles, 1)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'blog/article_list.html', {'articles': page_obj})

def contact_us(request):
    if request.method == 'POST':
        form = MassageForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data.get('name')
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # email = form.cleaned_data.get('email')
            # Message.objects.create(name=name, title=title, content=content, email=email)
            # tamami kar haie bala ro mitonim b sorat kholse shde mesl zir benevisim v dar data base save konim
            form.save()

            # hala ag mikhahim roye iki az in field ha taqirati emal konim b sorat zir amal mikonim
            # instance = form.save(commit=False)
            # instance.name  = "amir" ==>> ba inkar miaim name kar bar ro qabl azinke dar data base save beshe b amir taqir bedim v ya az  in ravesh braye baqie taqirat estefade komnim
            #
    else:
        form = MassageForm()
    return render(request , 'blog/contact_us.html' ,    {'form': form})



# tamrin :

# class ArticleListView(View):
#     # noinspection PyMethodMayBeStatic
#     def get(self, request):
#         page_obj = Article.objects.all()
#         return render(request , 'blog/article_list.html' , {'articles' : page_obj })



# class ArticleListTemplateView(TemplateView):
#     template_name = 'blog/article_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Article.objects.all()
#         return context



# class ArticleCounterRedirectView(RedirectView):
#
#     permanent = False
#
#     query_string = True
#
#     pattern_name = "article-detail"
#
#     def get_redirect_url(self, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs["pk"])
#         article.update_counter()
#         return super().get_redirect_url(*args, **kwargs)
