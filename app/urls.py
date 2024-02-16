from django.urls import path
from api.views import (
    CategoryCreateView,
    CategoryListView,
    CategoryById,
    AuthorCreateView,
    AuthorByIdView,
    AuthorListView,
    LibrarianCreateView,
    LibrarianListView,
    LibrarianByIdView,
    LibraryCreateView,
    LibraryListView,
    LibraryByIdView,
    BookCreateView,
    BookListView,
    BookByIdView,
    BookByCategoryListView,
    ExportCSVView,
    ExportToExcel
    )



urlpatterns =[
   
    path('create-category/',CategoryCreateView.as_view(),name='create-category'),
    path('list-category/',CategoryListView.as_view(),name='list-category'),
    path('category/<int:pk>/',CategoryById.as_view(),name='category-by-id'),
    path('create-author/',AuthorCreateView.as_view(),name='create-category'),
    path('list-author/',AuthorListView.as_view(),name='list-author'),
    path('author/<int:pk>/',AuthorByIdView.as_view(),name='author-by-id'),
    path('create-librarian/',LibrarianCreateView.as_view(),name='create-librarian'),
    path('list-librarian/',LibrarianListView.as_view(),name='list-librarian'),
    path('librarian/<int:pk>/',LibrarianByIdView.as_view(),name='librarian-by-id'),
    path('create-library/',LibraryCreateView.as_view(),name='create-library'),
    path('list-library/',LibraryListView.as_view(),name='list-library'),
    path('library/<int:pk>/',LibraryByIdView.as_view(),name='library-by-id'),
    path('create-book/',BookCreateView.as_view(),name='create-book'),
    path('list-book/',BookListView.as_view(),name='list-book'),
    path('book/<int:pk>/',BookByIdView.as_view(),name='book-by-id'),
    path('books/category/', BookByCategoryListView.as_view(), name='books-by-category'),
    path('export-books-csv/', ExportCSVView.as_view(), name='export_books_csv'),
    path('export-books-xl/', ExportToExcel.as_view(), name='export_books_excel'),

]

