from django.test import TestCase

from djbookshelf.models import ISBN


class TestISBN(TestCase):
    @classmethod
    def setUp(self):
        # Real one
        ISBN.objects.create(isbn="9788817016308")
        ISBN.objects.create(isbn="8817016306")

        # Fake one
        ISBN.objects.create(isbn="881701eeeee6306")

    def test_isbn_book_correct(self):
        lista = ["9788817016308", "8817016306"]
        for e in ISBN.objects.filter(isbn__in=lista):
            runned, created = e.elaborate()
            self.assertEqual(runned, True)
            self.assertEqual(created, True)
        for e in ISBN.objects.filter(isbn__in=lista):
            runned, created = e.elaborate()
            self.assertEqual(runned, False)
            self.assertEqual(created, False)

    def test_isbn_book_not_correct(self):
        lista = ["881701eeeee6306"]
        for e in ISBN.objects.filter(isbn__in=lista):
            runned, created = e.elaborate()
            self.assertEqual(runned, True)
            self.assertEqual(created, False)
        for e in ISBN.objects.filter(isbn__in=lista):
            runned, created = e.elaborate()
            self.assertEqual(runned, False)
            self.assertEqual(created, False)
