from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import generics

from library.models import Book, LibUser, RentBook, BookCategory
from library.serializers import BookCategorySerializer, BookSerializer, LibUserSerializer, RentBookSerializer


# veiwset: list, create, retrieve, update, partial_update, destroy

class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class LibUserViewSet(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer

class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer

# GET
class BookCategoryListView(generics.ListAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

# POST
class BookCategoryCreateView(generics.CreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

# GET and POST
class BookCategoryListCreateView(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

# GET
class BookCategoryRetriveView(generics.RetrieveAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

# PUT
class BookCategoryUpdateView(generics.UpdateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

# GET and PUT
class BookCategoryRetriveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

# DELETE
class BookCategoryDestroyView(generics.DestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

# DELETE and PUT
class BookCategoryRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    