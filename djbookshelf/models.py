import logging

from django.db import models

from djbookshelf.exceptions import ISBNNoBookFoundException
from djbookshelf.utility import get_book_from_isbn

log = logging.getLogger(__name__)


class Author(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    author = models.ForeignKey(
        Author, null=True, blank=True, on_delete=models.CASCADE
    )
    image = models.URLField(null=True, blank=True)

    room = models.CharField(max_length=200, blank=True, null=True)
    shelf = models.CharField(max_length=200, blank=True, null=True)
    book_code = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.author} - {self.title}"


class ISBN(models.Model):
    isbn = models.CharField(max_length=13, blank=True, null=True)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, null=True, blank=True
    )
    searched_google = models.BooleanField(default=False)

    def __str__(self):
        if self.book:
            return self.isbn
        return f"{self.isbn} - {self.book}"

    def elaborate(self) -> (bool, bool):
        if not self.searched_google:
            flag = None
            try:
                data = get_book_from_isbn(self.isbn)

                author, _ = Author.objects.get_or_create(name=data["author"])
                book = Book.objects.create(
                    title=data["title"], author=author, image=data["image"]
                )
                self.book = book
                flag = True
            except ISBNNoBookFoundException:
                log.info(f"{self.isbn} not found")
                flag = False
            finally:
                self.searched_google = True
                self.save()
                return True, flag
        return False, False
