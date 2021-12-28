from typing import Union

from django.db import models
from isbnlib import meta, cover, NotValidISBNError

from djbookshelf.exceptions import ISBNNoBookFoundException

ISBN_SEARCH = ["goob", "openl", "wiki"]


def get_data_book(isbn: str) -> dict:
    try:
        for engine in ISBN_SEARCH:
            data = meta(isbn, engine)
            if data != {}:
                return data
        raise ISBNNoBookFoundException
    except NotValidISBNError:
        raise ISBNNoBookFoundException


def get_book_from_isbn(isbn: Union[str, models.CharField]) -> dict:
    image = None
    cover_data = cover(isbn)
    if cover_data.get("thumbnail", None):
        image = cover_data["thumbnail"]
    elif cover_data.get("smallThumbnail", None):
        image = cover_data["smallThumbnail"]

    data = get_data_book(isbn)

    return {
        "title": data.get("Title", ""),
        "authors": data.get("Authors", []),
        "publication_date": data.get("Year", ""),
        "image": image,
        "language": data.get("Language", ""),
        "publisher": data.get("Publisher", ""),
    }
