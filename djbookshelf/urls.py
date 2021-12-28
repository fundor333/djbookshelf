from django.urls import path
from django.views.generic import TemplateView

app_name = "djbookshelf"


class DashBoard(TemplateView):
    template_name = "djbookshelf/core.html"


urlpatterns = [
    path("dashboard/", DashBoard.as_view(), name="dashboard"),
    path(
        "",
        DashBoard.as_view(),
    ),
]
