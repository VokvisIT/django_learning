from django.db import models
from django.db.models import Count

QUESTION_TYPES = (
        ('single_choice', 'Одиночный выбор'),
        ('multiple_choice', 'Множественный выбор'),
        ('open', 'Открытый вопрос'),
    )

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return self.question_text.title()

class Choice(models.Model):
    """Класс для набора разных вариантов ответа на single_choice и multiple_choice"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text.title()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    answer_text = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice or self.answer_text}'