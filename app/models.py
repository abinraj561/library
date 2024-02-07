from django.db import models


class Author(models.Model):
    author_name=models.CharField(max_length=100)


class Category(models.Model):
    name=models.CharField(max_length=100)


class Librarian(models.Model):
    name=models.CharField(max_length=100)


class Library(models.Model):
    name=models.CharField(max_length=100)
    librarian=models.ForeignKey(Librarian,on_delete=models.CASCADE)
    address=models.TextField()
    
    
class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    published_on=models.DateField()
    copies_available=models.PositiveIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    language=models.CharField(max_length=100)
    pages=models.PositiveIntegerField()
    library=models.ForeignKey(Library,on_delete=models.CASCADE)
