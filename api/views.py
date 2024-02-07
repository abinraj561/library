from rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from django.db.models import Q
from app.models import(
    Author,
    Category,
    Librarian,
    Library,
    Book
)
from app.serializers import(
    CategorySerializer,
    AuthorSerializer,
    LibrarianSerializer,
    LibrarySerializer,
    BookSerializer
)


#Category-Create
class CategoryCreateView(generics.CreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({"message":"Category added Successfully","data":serializer.data},status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response ({"message":"Error in creating Category"},status=status.HTTP_304_NOT_MODIFIED)


#Category List
class CategoryListView(generics.ListAPIView):
    try:
        queryset=Category.objects.all()
        serializer_class=CategorySerializer
        permission_classes=[permissions.AllowAny]
    except Exception as e:
        raise Response({"Error":"Check the given credentials"})


#Category -Retrieve-Update-Delete
class CategoryById(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[permissions.IsAdminUser]
    
    def update(self, request, *args, **kwargs):
        try:
            instance=self.get_object()
            serializer=self.get_serializer(instance,data=request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            updated_instance=serializer.save()
            serialized_data=self.get_serializer(updated_instance).data
            return Response({"message":"Updated Successfully","data":serialized_data},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message":"Error in updating Category"},status=status.HTTP_304_NOT_MODIFIED)


    def delete(self, request, *args, **kwargs):
        try:
            response=super().delete(request, *args, **kwargs)
            return Response({"message":"Category deleted successfully"},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message":"Failed to delete Category"})


#Author-Create
class AuthorCreateView(generics.CreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    permission_classes=[permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        try:
            serializer=self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({"message":"Author created Successfully","data":serializer.data},status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"message":"Error in creating Author"},status=status.HTTP_304_NOT_MODIFIED)
        
        
#Author List
class AuthorListView(generics.ListAPIView):
    try:
        queryset=Author.objects.all()
        serializer_class=AuthorSerializer
        permission_classes=[permissions.AllowAny]
    
    except Exception as e:
        raise Response({"Error":"Check the given credentials"})


#Author Retrieve-Update-Delete
class AuthorByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    permission_classes=[permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        try:
            instance=self.get_object()
            serializer=self.get_serializer(instance,data=request.data,partial=True)
            serializer.is_valid()
            updated_instance=serializer.save()
            serialized_data=self.get_serializer(updated_instance).data
            return Response({"message":"Author updated successfully","data":serialized_data},status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"message":"Error in Updating author"},status=status.HTTP_304_NOT_MODIFIED)
        

    def delete(self, request, *args, **kwargs):
        try:
            response= super().delete(request, *args, **kwargs)
            return Response({"message":"Error in deleting"},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message":"Error in deleting Author"})


#Librarian -Create
class LibrarianCreateView(generics.CreateAPIView):
    queryset=Librarian.objects.all()
    serializer_class=LibrarianSerializer
    permission_classes=[permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            serializer=self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({"message":"Librarian Created Successfully","data":serializer.data},status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"message":"Error in creating Librarian"},status=status.HTTP_304_NOT_MODIFIED)


#Librarian List
class LibrarianListView(generics.ListAPIView):
    try:
        queryset=Librarian.objects.all()
        serializer_class=LibrarianSerializer
        permission_classes=[permissions.AllowAny]

    except Exception as e:
        raise Response({"Error":"Check the given credentials"})
    
    
#Librarian Update-Retrieve-Delete
class LibrarianByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Librarian.objects.all()
    serializer_class=LibrarianSerializer
    permission_classes=[permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        try:
            instance=self.get_object()
            serializer=self.get_serializer(instance,data=request.data,partial=True)
            serializer.is_valid()
            updated_instance=serializer.save()
            serialized_data=self.get_serializer(updated_instance).data
            return Response({"message":"Librarian updated successfully","data":serialized_data},status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"mssage":"Error in updating Librarian"},status=status.HTTP_304_NOT_MODIFIED)
        

    def delete(self, request, *args, **kwargs):
        try:

            response=super().delete(request, *args, **kwargs)
            return Response({"message":"Deleted Successfully"},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message":"Error in deleting LIbrarian"})
        

#Library -create
class LibraryCreateView(generics.CreateAPIView):
    queryset=Library.objects.all()
    serializer_class=LibrarySerializer
    permission_classes=[permissions.IsAdminUser]


    def create(self, request, *args, **kwargs):
        try:
            serializer=self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({"message":"Library created Successfully","data":serializer.data},status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"message":"Error in creating library"})
        

#Library List   
class LibraryListView(generics.ListAPIView):
    try:
        queryset=Library.objects.all()
        serializer_class=LibrarySerializer
        permission_classes=[permissions.AllowAny]

    except Exception as e:
        raise Response({"Error":"Check the given credentials"})
    

#Update-Retrieve-Edit Library
class LibraryByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Library.objects.all()
    serializer_class=LibrarySerializer
    permission_classes=[permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        try:
            instance=self.get_object()
            serializer=self.get_serializer(instance,data=request.data,partial=True)
            serializer.is_valid()
            updated_instance=serializer.save()
            serialized_data=self.get_serializer(updated_instance)
            return Response({"message":"Updated Successfully","data":serialized_data},status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"message":"Error in updating library"},status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)  
            return Response({"message":"deleted succsessfully"},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message":"Error in deleting Library"})
        

#create -Book
class BookCreateView(generics.CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        try:
            serializer=self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({"message":"Book created Successfully","data":serializer.data},status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"message":"Error in creating serializer"},status=status.HTTP_304_NOT_MODIFIED)
        

#Book total list
class BookListView(generics.ListAPIView):
    try:
        queryset=Book.objects.all()
        serializer_class=BookSerializer
        permission_classes=[permissions.AllowAny]

    except Exception as e:
        raise Response({"Error":"Check the given credentials"})
    

#Book category-wise
class BookByCategoryListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes=[permissions.AllowAny]

    def get_queryset(self):
        try:
            category_id = self.request.query_params.get('category_id', None)
            category_name = self.request.query_params.get('category_name', None)

            queryset = Book.objects.all()

            if category_id:
                queryset = queryset.filter(category_id=category_id)

            if category_name:
                queryset = queryset.filter(category__name__iexact=category_name)

            return queryset
        
        except Exception as e:
            return Response({"Error":"Check the given data and try again"})
        

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            total_count = queryset.count()
            serializer = self.get_serializer(queryset, many=True)

            data = {
                'total_count': total_count,
                'books': serializer.data
            }

            return Response(data)
        
        except Exception as e:
            return Response({"Error":"Check the given data and try again"})


#book -id wise
class BookByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        try:
            instance=self.get_object()
            serializer=self.get_serializer(instance,data=request.data,partial=True)
            serializer.is_valid()
            updated_instance=serializer.save()
            serialized_data=self.get_serializer(updated_instance)
            return Response({"message":"Updated Successfully","data":serialized_data},status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"message":"Error in updation"})
        

    def delete(self, request, *args, **kwargs):
        try:
            response= super().delete(request, *args, **kwargs)
            return Response({"message": "Deleted successfully"},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message":"Error in deletion of Book"})
        

