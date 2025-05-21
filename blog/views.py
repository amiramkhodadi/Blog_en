from django.shortcuts import render,get_object_or_404

from blog.models import Article




def article_detail(request , pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request , 'blog/post_details.html',{'article' : article })