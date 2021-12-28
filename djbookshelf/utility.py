import json
from typing import Union

import requests
from django.db import models

from djbookshelf.exceptions import ISBNNoBookFoundException, ISBNJsonException


def get_book_from_isbn(isbn: Union[str, models.CharField]) -> dict:
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    try:
        book_data = response.json()
        if book_data.get("totalItems", -1) == 0:
            raise ISBNNoBookFoundException
        volume_info = book_data["items"][0]["volumeInfo"]
        author = volume_info["authors"]
        prettify_author = author if len(author) > 1 else author[0]

        image = None
        if volume_info.get("imageLinks", None):
            if volume_info["imageLinks"].get("thumbnail", None):
                image = volume_info["imageLinks"]["thumbnail"]
            elif volume_info["imageLinks"].get("smallThumbnail", None):
                image = volume_info["imageLinks"]["smallThumbnail"]

        return {
            "title": volume_info["title"],
            "author": prettify_author,
            "publication_date": volume_info["publishedDate"],
            "image": image,
        }
    except (json.JSONDecodeError, ValueError):
        raise ISBNJsonException
