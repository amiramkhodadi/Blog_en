from django.urls import reverse
from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        # dar admin panel in modelo b do shekle mofrad v jam seda zade mishe v ma baid braye shakhsi sazi behesh bgim k mofrd v jame on chi jori bashe
        verbose_name = "  دسته بندی "
        verbose_name_plural = "دسته بندی ها"


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


class Meta:
    # braye order sazi az hmon order by estefade konim kheili bhtre v inja faqat jane amozeshi v kar ba meta ro dare v ba search zadan meta class in django mitonim bishtr rajeb in class ettelaat kasb konim
    ordering = ['-created_date']
    # verbose_name = 'X' ==>> to admin panel dg model ha b esm X seda zade mishan
    # verbose_name_plural = 'Xes' ==>> to admin panel zamani k majmoeii az X ha ro dashte bashnd v b ma onaro Xes moarefi mikone v ma
    # in do mord bala braye shakhsi sazi  and v braye modriat b zaban farsi besyar kar amad and



class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='articles')
    category = models.ManyToManyField(Category , related_name='articles')
    floatfield = models.FloatField(default=1)
    myfile = models.FileField(upload_to='blog/file/')
    status = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    objects = models.Manager()
    custom_objects = ArticleManager()
    slug = models.SlugField(unique=True , blank=True)

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.slug])

    def save(self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,):

       self.slug = slugify(self.title)
       super(Article, self).save()

        # class Meta:
        #     ordering = ['-created_date']

    class Meta:
            # dar admin panel in modelo b do shekle mofrad v jam seda zade mishe v ma baid braye shakhsi sazi behesh bgim k mofrd v jame on chi jori bashe
            verbose_name = " مقاله "
            verbose_name_plural = "مقالات "




    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url} " width="60" height="50" />')
        return format_html("<h3 style = 'color:red '> no picture</h3>")
    show_image.short_description = 'تصویر مقاله'



    # author = models.ForeignKey(User, on_delete=models.SET_NULL , null = True) ==>> bramavaqeiik ma dos ndrim data haye pak beshan
    # author = models.ForeignKey(User, on_delete=models.SET_DEFAULT , default = 'id another user') ==>> bramavaqeiik ma dos ndrim data haye pak beshan v malekiat ono b fard dg ii ba estefade az id ono pass midim
    # author = models.ForeignKey(User, on_delete=models.PROTECT) ==>> az ma mikhad k ag bkhaim usero pak konim miporse k ba post haye on baid chi kar konim
    # pub_date = models.DateField(default=timezone.now())  ==> , unique_for_date='pub_date'
    def __str__(self):
        return f'{self.title} -{self.created_date}'


class Comment (models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE,related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
            # dar admin panel in modelo b do shekle mofrad v jam seda zade mishe v ma baid braye shakhsi sazi behesh bgim k mofrd v jame on chi jori bashe
            verbose_name = " نظر "
            verbose_name_plural = "نظرات "

    def __str__(self):
        return f'{self.author} - {self.content}'

class Message(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)


    class Meta:
            # dar admin panel in modelo b do shekle mofrad v jam seda zade mishe v ma baid braye shakhsi sazi behesh bgim k mofrd v jame on chi jori bashe
            verbose_name = " پیام "
            verbose_name_plural = " پیام ها  "

    def __str__(self):
        return f'{self.name} , {self.title} '

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='likes')
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها "
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.user} - {self.article}'