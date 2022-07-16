from tokenize import Name
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView,ListView,CreateView,DetailView,UpdateView,DeleteView
from . models import Book,Author
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from assesment.serializers import AuthorSerializer,BookSerializer

# Create your views here.


@csrf_exempt
def bookApi(request):
    if request.method=='GET':
        books = Book.objects.all()
        books_serializer=BookSerializer(books,many=True)
        return JsonResponse(books_serializer.data,safe=False)
    elif request.method=='POST':
        books_data=JSONParser().parse(request)
        books_serializer=BookSerializer(data=books_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse('Failed to Add',safe=False)
    # elif request.method=='PUT':
    #     books_data=JSONParser().parse(request)
    #     book=Book.objects.get(name=books_data['name'])
    #     books_serializer=BookSerializer(book,data=books_data)
    #     if books_serializer.is_valid():
    #         books_serializer.save()
    #         return JsonResponse('Update Successfully',safe=False)
    #     return JsonResponse('Failed to Update')
    # elif request.method=='DELETE':
    #     book=Book.objects.get(name=id)
    #     book.delete()
    #     return JsonResponse('Delete Successfully',safe=False)

@csrf_exempt
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        book_serializer = BookSerializer(book)
        return JsonResponse(book_serializer.data)
  
    elif request.method == 'PUT':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(book, data=book_data)
  
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data)
        return JsonResponse(book_serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)



@csrf_exempt
def AuthorApi(request,id=0):
    if request.method=='GET':
        author = Author.objects.all()
        author_serializer=AuthorSerializer(author,many=True)
        return JsonResponse(author_serializer.data,safe=False)
    elif request.method=='POST':
        author_data=JSONParser().parse(request)
        author_serializer=AuthorSerializer(data=author_data)
        if author_serializer.is_valid():
            author_serializer.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse('Failed to Add',safe=False)
    # elif request.method=='PUT':
    #     author_data=JSONParser().parse(request)
    #     author=Author.objects.get(author_id=author_data['author_id'])
    #     author_serializer=AuthorSerializer(author,data=author_data)
    #     if author_serializer.is_valid():
    #         author_serializer.save()
    #         return JsonResponse('Update Successfully',safe=False)
    #     return JsonResponse('Failed to Update')
    # elif request.method=='DELETE':
    #     author=Author.objects.get(author_id=id)
    #     author.delete()
    #     return JsonResponse('Delete Successfully',safe=False)


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