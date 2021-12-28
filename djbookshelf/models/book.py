from django.db import models

import logging

log = logging.getLogger(__name__)


class Book(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    authors = models.ManyToManyField("Author")
    language = models.ForeignKey(
        "Language", null=True, blank=True, on_delete=models.CASCADE
    )
    publisher = models.ForeignKey(
        "Publisher", null=True, blank=True, on_delete=models.CASCADE
    )
    year = models.CharField(max_length=6, null=True, blank=True)
    image = models.URLField(null=True, blank=True)

    room = models.CharField(max_length=200, blank=True, null=True)
    shelf = models.CharField(max_length=200, blank=True, null=True)
    book_code = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.author} - {self.title}"
