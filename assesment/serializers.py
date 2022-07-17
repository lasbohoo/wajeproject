from rest_framework import serializers
from .models import Book,Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'


class BookSerializer(serializers.ModelSerializer):
    
    author = AuthorSerializer()
    class Meta:
        model=Book
        fields='__all__'






    # def create(self, validated_data):
    #     author = Author.objects.get(pk=validated_data.pop('author'))
    #     book = Book.objects.create(**validated_data)
    #     Author.objects.create(book=book, **author)
    #     return book

