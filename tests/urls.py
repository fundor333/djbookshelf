from django.urls import include, path

urlpatterns = [path("bookshelf", include("djbookshelf.urls"))]
