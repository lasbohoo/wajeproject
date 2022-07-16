from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name="book")

    def __str__(self):
        return f'{self.id} {self.author.first_name}'

