from django.shortcuts import render

from blog.models import Article


# Create your views here.
def home(request):
    articles = Article.objects.all()
    return render(request, 'home/index.html',{'articles':articles})