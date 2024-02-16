from django.core.management.base import BaseCommand
from app.models import *
from faker import Faker
fake= Faker()

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            author = Author.objects.get(id=7)
            category = Category.objects.get(id=5)
            library = Library.objects.get(id=2)

            books_to_create = [
                Book(
                    title=("Oh my god"),
                    published_on=fake.date_between(start_date='-1y', end_date='today'),
                    author=(author),
                    category=(category),
                    copies_available=(450),
                    pages=(500),
                    language=(["English"]),
                    library=(library)
                ),
                ]

            Book.objects.bulk_create(books_to_create)

            return "success"
        
        except Exception as e:

           self.stderr.write(self.style.ERROR(f'Error during script execution: {str(e)}'))