from django.apps import AppConfig


class MygramConfig(AppConfig):
    name = 'mygram'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Profile'))

