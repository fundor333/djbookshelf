from django.db import models


class Author(models.Model):
    name = models.CharField(max_lenght=300, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    author = models.ForeignKey(Author, null=True, blank=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    room = models.CharField(max_length=200, blank=True, null=True)
    shelf = models.CharField(max_length=200, blank=True, null=True)
    book_code = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.author} - {self.title}"
