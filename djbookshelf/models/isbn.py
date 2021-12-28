from django.db import models

from djbookshelf.exceptions import ISBNNoBookFoundException
from djbookshelf.models.author import Author
from djbookshelf.models.book import Book
from djbookshelf.models.publisher import Publisher
from djbookshelf.models.language import Language
from djbookshelf.utility import get_book_from_isbn
import logging

log = logging.getLogger(__name__)


class ISBN(models.Model):
    isbn = models.CharField(max_length=13, blank=True, null=True)
    book = models.ForeignKey(
        "Book", on_delete=models.CASCADE, null=True, blank=True
    )
    searched = models.BooleanField(default=False)

    def __str__(self):
        if self.book:
            return self.isbn
        return f"{self.isbn} - {self.book}"

    def elaborate(self) -> (bool, bool):
        if not self.searched:
            flag = False
            try:
                data = get_book_from_isbn(self.isbn)
                if data.get("language", "") != "":
                    language, _ = Language.objects.get_or_create(
                        name=data["language"]
                    )
                else:
                    language = None
                if data.get("publisher", "") != "":
                    publisher, _ = Publisher.objects.get_or_create(
                        name=data["publisher"]
                    )
                else:
                    publisher = None
                book = Book.objects.create(
                    title=data["title"],
                    image=data["image"],
                    year=data["publication_date"],
                    publisher=publisher,
                    language=language,
                )
                self.book = book
                for a in data["authors"]:
                    author, _ = Author.objects.get_or_create(name=a)
                    book.authors.add(author)
                flag = True
                book.save()
            except ISBNNoBookFoundException:
                log.error(f"{self.isbn} not found")
                flag = False
            self.searched = True
            self.save()
            return True, flag
        return False, False
