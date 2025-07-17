from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    # dar in qesmta mitonim esm header in app dar panel admin ro taqir bedim
    verbose_name = 'بلاگ ها '

