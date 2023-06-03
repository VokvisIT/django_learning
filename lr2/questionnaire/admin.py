from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from .models import Question, Choice, Answer

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'question_type')
    inlines = [ChoiceInline]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice', 'text')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Answer, AnswerAdmin)