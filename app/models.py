from django.db import models

class CommonFields(models.Model):
    name = models.CharField(max_length=100,null=True)
    
    class Meta:
        abstract = True

class Author(CommonFields):
    pass

class Category(CommonFields):
    pass

class Librarian(CommonFields):
    pass

class Library(CommonFields):
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    address = models.TextField()

class Book(CommonFields):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    published_on = models.DateField()
    copies_available = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    pages = models.PositiveIntegerField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
