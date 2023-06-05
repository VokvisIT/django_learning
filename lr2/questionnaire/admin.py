from django.contrib import admin

from questionnaire.models import Answer, Choice, Poll, Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'question_type', 'num_answers', 'poll')
    list_display_links = "id", "question_text",
    ordering = "id",

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text')
    list_display_links = 'id', 'question',
    ordering = "id",

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice', 'answer_text')
    list_display_links = 'id',
    ordering = "id",
class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'poll_title', 'count_comp')
    list_display_links = 'id',
    ordering = "id",

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Poll, PollAdmin)