from django.contrib import admin
from .models import Poll, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    list_display = ['id','poll_title', 'completed_count']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','poll', 'question_text', 'question_type']
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id','question', 'choice_text', 'answer_count']



admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
