from rest_framework import serializers
from app.models import(
    Author,
    Category,
    Librarian,
    Library,
    Book
)


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields ="__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields="__all__"

    
class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model= Librarian
        fields="__all__"
        


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model= Library
        fields="__all__"



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"