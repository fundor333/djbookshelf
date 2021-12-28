from django.db import models
import logging

log = logging.getLogger(__name__)


class Language(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name
