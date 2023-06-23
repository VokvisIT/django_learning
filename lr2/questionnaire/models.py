from django.db import models
from django.db.models import Count

QUESTION_TYPES = (
        ('single_choice', 'Одиночный выбор'),
        ('multiple_choice', 'Множественный выбор'),
        ('open', 'Открытый вопрос'),
    )
class Poll(models.Model):
    poll_title = models.TextField(max_length=50, null=False, blank=True)
    completed_count = models.IntegerField(default=0)

class Question(models.Model):
    question_text = models.TextField(max_length=100, null=True, blank=True)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

class Choice(models.Models):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=100, null=True, blank=True)
    answer_count = models.IntegerField(default=0)