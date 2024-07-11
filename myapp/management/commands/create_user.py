from django.core.management.base import BaseCommand
from myproject.myapp.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User(name='Sergei', email='klap@yandex.ru', password='secret', age=27)
        user.save()
        self.stdout.write(f'{user}')