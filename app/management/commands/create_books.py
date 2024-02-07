from django.core.management.base import BaseCommand
from app.models import *
from faker import Faker
import random
fake= Faker()

class Command(BaseCommand):

    def handle(self, *args, **options):

        try:

            author = Author.objects.get(id=3)
            category = Category.objects.get(id=2)
            library = Library.objects.get(id=2)

            books_to_create = [
                Book(
                    title=fake.sentence(),
                    published_on=fake.date_between(start_date='-1y', end_date='today'),
                    author=random.choice(author),
                    category=random.choice(category),
                    copies_available=random.randint(1, 10),
                    pages=random.randint(100,1000),
                    language=random.choice(["Malaylam","English","Hindi"]),
                    library=random.choice(library)
                ),
                ]


            Book.objects.bulk_create(books_to_create)

            return "success"
        
        except Exception as e:

           self.stderr.write(self.style.ERROR(f'Error during script execution: {str(e)}'))