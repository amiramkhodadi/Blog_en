from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
    # dar in qesmta mitonim esm header in app dar panel admin ro taqir bedim
    verbose_name = "حساب ها "
