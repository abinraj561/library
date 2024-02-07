from django.core.management.base import BaseCommand
from app.models import *
from faker import Faker
import random
fake= Faker()

class Command(BaseCommand):

    def handle(self, *args, **options):

        try:
            librarian = Librarian.objects.all()
            

            Library_to_create = [
                Library(
                    name=fake.sentence(),
                    librarian=random.choice(librarian),
                    address=fake.sentence()
                            )
            ]


            Library.objects.bulk_create(Library_to_create)

            return "success"
        
        except Exception as e:

           self.stderr.write(self.style.ERROR(f'Error during script execution: {str(e)}'))