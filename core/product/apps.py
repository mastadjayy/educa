from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
    label = 'core_product'
    verbose_name = 'App: Product'
    verbose_name_plural = 'App: Products'
