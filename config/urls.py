from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from .health import health


urlpatterns = [
    path("", RedirectView.as_view(url="/admin/", permanent=False)),
    path("admin/", admin.site.urls),
    path("healthz/", health, name="health"),
]
