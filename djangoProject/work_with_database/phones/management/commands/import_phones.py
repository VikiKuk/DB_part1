# import csv
#
# from django.core.management.base import BaseCommand
# from phones.models import Phone


# class Command(BaseCommand):
#     def add_arguments(self, parser):
#         pass
#
#     def handle(self, *args, **options):
#         with open('phones.csv', 'r') as file:
#             phones = list(csv.DictReader(file, delimiter=';'))
#
#         for phone in phones:
#             # TODO: Добавьте сохранение модели
#             pass


import csv
from django.core.management.base import BaseCommand

from phones.models import Phone


class Command(BaseCommand):
    help = 'Импорт из csv'

    def handle(self, *args, **options):
        try:
            with open('phones.csv', mode='r') as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    Phone.objects.update_or_create(
                        id=row['id'],
                        defaults={
                            'name': row['name'],
                            'price': row['price'],
                            'image': row['image'],
                            'release_date': row['release_date'],
                            'lte_exists': row['lte_exists'],
                        }
                    )
            self.stdout.write(self.style.SUCCESS('Импорт успешен'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))