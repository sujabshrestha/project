from django.apps import AppConfig


class SellerConfig(AppConfig):
    name = 'seller'


    def ready(self):
        import seller.signals