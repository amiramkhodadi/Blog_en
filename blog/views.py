from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.defaulttags import querystring
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, RedirectView, FormView, ListView, DetailView

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



# class ArticleRedirectView(RedirectView):
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
#
# class ArticleListView(ListView):
#             ba tavajoh b model zir miad y listy az khorojo b ma tahvil mide
#     model = Article
#              code paiin bra zamanie k ma esmi k b template pass midimo baid inja benevisim
#     context_object_name = 'articles'
#              ag b sorat drst esm template mesl : article_list.html benevisim dg niazi nis  k esm template ro besh bedim dar qeir in sorat baid bhsh bgim k dar kodom template khoro ji ro be ma neshon  bde
#     template_name = 'blog/article_list.html'
#                 ba hmin y khat code cofie k bgim k chnd ta X dar safe ma bashnd
#                 az page_obj b onvan vorodi dar qesmat tag haye html baid estefade konim ta b drsty kar kone
#     paginate_by = 1  # if pagination is desired
#                 ag niazi b shart gozari dar list jahat namayesh dashte bashim ba query set onaro modriat mikonim
#     queryset = Article.objects.filter()
#
#     ag bkhahim k joda az data ii k khodesh az model migire chiz dg ii hm behesh ezafe konim az def pain estefade mikonim  mannd zir
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["now"] = timezone.now()
#         return context


# class ArticleDetailView(DetailView):
#             ag az qabl hme chiz ro rayat krde bashim ba hmin y khat code paiin jozayat b sadegi b ma namayesh dade mishand
#     model = Article
#                 dar halamt mannol k dar nazr migire k esm file b sorat modelname_detail,html hastesh vli ag chize dg ii bod inja baid behesh bgim
#     # template_name = 'blog/article_detail.html'
#             dar halat mamol dar template baid az hmin esm model v onvan vorodi jahat por krdn feild ha estefade konim vli ag vorodi template bkhaim chize dg ii bashe inja badi meqdar dehi beshe
#     context_object_name = 'article'
#         dar hengam namayesh jozayat posty ag bkhahim filter v ya sharty braye on post dashte bashim   az  in ravesh estefade mikonim
#     queryset = Article.objects.filter()
#             dar halat mamol <int  : pk > ==>> minevism vli ag jaye pk chiz dg neveshtim inja baid bhsh moarefi konim
#     pk_url_kwarg = 'pk'
#     ag <slug:X> ==>> dar halat mamol b jaye X slug minevisim dar qeir in sorat baid paiin esmesho moarefi konim
#     slug_url_kwarg = 'slug'
#             ag field slugi k dar model hamon moarefi krde im esmi b qeir az slug dashte bashnad inja baid behsh bgim chie
#     slug_field = 'slug'
#
#         ag bkhahim joda az detail chizi ezafe tar ham vared template konim az in def paiin estefade mikonim
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['name'] = "AMIR"



# class ContectUsFormView(FormView):
#             form k qarre sakhte beshe bar asas kodm mode form bashe 1
#     form_class = MassageForm
#             mige k form maro koja besaze
#     template_name = 'blog/contact_us.html'
#             bara zamani k form ma b drsty kar krd v valid bod v data dar data base save shd  ma b in masir hedayat mishim
#     success_url = '/'
#              baraye save krdn form to data base
#     def form_valid(self, form):
#         form_data = form.cleaned_data
#         Message.objects.create(**form_data)
#         return super().form_valid(form)
#
#
#



