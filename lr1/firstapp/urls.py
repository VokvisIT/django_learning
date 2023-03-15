from django.urls import path
from .views import index, special
appname = "firstapp"

urlpatterns = [
    path("", index, name="index"),
    path("special/", special, name="special"),
]