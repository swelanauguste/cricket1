
from django.core.management.base import BaseCommand

from users.models import Role


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                name = row.replace('\n', '').upper()
                self.stdout.write(self.style.SUCCESS(f'{name} added'))
                customer = Role.objects.get_or_create(
                    name=name)
