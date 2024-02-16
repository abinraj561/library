from django.core.management.base import BaseCommand
from app.models import *
import random

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            category_to_create = [
                Category(
                    name=random.choice(["Romance","Narration","Profile"])
                            ),
            ]
            Category.objects.bulk_create(category_to_create)
            return "success"
        
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error during script execution: {str(e)}'))