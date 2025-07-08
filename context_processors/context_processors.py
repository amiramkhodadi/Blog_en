from blog.models import Article, Category


def recent_articles(request):
    recent_articles = Article.objects.all().order_by('-created_date')[:3]
    categories = Category.objects.all()
    return {'recent_articles': recent_articles , 'categories': categories}