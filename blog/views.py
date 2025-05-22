from django.shortcuts import render,get_object_or_404

from blog.models import Article




def article_detail(request , slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request , 'blog/post_details.html',{'article' : article })