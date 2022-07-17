from rest_framework import status
from rest_framework import serializers
from django.shortcuts import render, HttpResponse
from . models import Book,Author
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from assesment.serializers import AuthorSerializer,BookSerializer
from rest_framework.response import Response

# Create your views here.




@api_view(['GET', 'POST'])
@csrf_exempt
def bookApi(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        print(book_serializer)
        return Response(book_serializer.data)

    elif request.method == 'POST':
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def book_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        book = Book.objects.get(pk=pk)
        
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        book_serializer = BookSerializer(book)
        return Response(book_serializer.data)

    elif request.method == 'PUT':
        book_serializer = BookSerializer(instance=book, data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST'])
@csrf_exempt
def authorApi(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        author = Author.objects.all()
        author_serializer = AuthorSerializer(author, many=True)
        return Response(author_serializer.data)

    elif request.method == 'POST':
        author_serializer = AuthorSerializer(data=request.data)
        if author_serializer.is_valid():
            author_serializer.save()
            return Response(author_serializer.data, status=status.HTTP_201_CREATED)
        return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        author_serializer = AuthorSerializer(author)
        return JsonResponse(author_serializer.data)
  
    elif request.method == 'PUT':
        author_data = JSONParser().parse(request)
        author_serializer = AuthorSerializer(author, data=author_data)
  
        if author_serializer.is_valid():
            author_serializer.save()
            return JsonResponse(author_serializer.data)
        return JsonResponse(author_serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        author.delete()
        return HttpResponse(status=204)