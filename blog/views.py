from django.shortcuts import render,get_object_or_404

from blog.models import Article


# Create your views here.
# def blog_post(request):
#     return render(request, 'blog/blog.html',{})

def article_detail(request , pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request , 'blog/post_details.html',{'article' : article })