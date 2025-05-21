from django.urls import reverse
from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager,self).get_queryset().filter(status=True)
    #
    # def counter(self):
    #
    #     return len(self.all())
    #
    # def published(self):
    #     return self.filter(published=True)



class Article(models.Model):
    title = models.CharField(max_length=200 ,editable=False ,help_text='enter your article title' )
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    floatfield = models.FloatField(default=1)
    myfile = models.FileField(upload_to='blog/file/')
    status = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    objects = models.Manager()
    custom_objects = ArticleManager()
    slug = models.SlugField(unique=True , blank=True)

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])

   def save(self , force_insert=False, force_update=False, using=None, update_fields=None):
       self.slug = slugify(self.title)
       super(Article, self).save()







    # author = models.ForeignKey(User, on_delete=models.SET_NULL , null = True) ==>> bramavaqeiik ma dos ndrim data haye pak beshan
    # author = models.ForeignKey(User, on_delete=models.SET_DEFAULT , default = 'id another user') ==>> bramavaqeiik ma dos ndrim data haye pak beshan v malekiat ono b fard dg ii ba estefade az id ono pass midim
    # author = models.ForeignKey(User, on_delete=models.PROTECT) ==>> az ma mikhad k ag bkhaim usero pak konim miporse k ba post haye on baid chi kar konim
    # pub_date = models.DateField(default=timezone.now())  ==> , unique_for_date='pub_date'
    def __str__(self):
        return f'{self.title} -{self.created_date}'