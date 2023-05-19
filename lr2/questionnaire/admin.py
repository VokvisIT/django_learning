from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from .models import DataSet

@admin.register(DataSet)
class DataSetAdmin(admin.ModelAdmin):
    list_display = "pk", "gender", "open_question"
    list_display_links = "pk",