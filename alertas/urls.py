from django.urls import path

from . import views


urlpatterns = [
    path("alt", views.index, name="index"),
]