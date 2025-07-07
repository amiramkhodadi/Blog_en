from blog.models import Article

def recent_articles(request):
    recent_articles = Article.objects.all().order_by('-created_date')[:3]
    return {'recent_articles': recent_articles}