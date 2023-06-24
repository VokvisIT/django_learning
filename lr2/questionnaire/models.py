from django.db import models
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

QUESTION_TYPES = (
        ('single_choice', 'Одиночный выбор'),
        ('multiple_choice', 'Множественный выбор'),
        ('open', 'Открытый вопрос'),
    )
class Poll(models.Model):
    poll_title = models.TextField(max_length=50, null=False, blank=True)
    completed_count = models.IntegerField(default=0)
    def __str__(self):
        return self.poll_title

class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.TextField(max_length=100, null=False, blank=True)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    def __str__(self):
        return self.question_text
    def save(self, *args, **kwargs):
           super().save(*args, **kwargs)
           if self.question_type == 'open':
               Choice.objects.create(question=self, choice_text=None)
           elif self.question_type in ['multiple_choice', 'single_choice']:
               Choice.objects.create(question=self, choice_text=None)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=100, null=True, blank=True)
    answer_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
    def get_percentage(self):
        total_count = self.question.choice_set.aggregate(Sum('answer_count'))['answer_count__sum']
        if total_count:
            percentage = (self.answer_count / total_count) * 100
            return round(percentage, 2)
        return 0
    def get_choice_text(self):
        if self.choice_text is None:
            return "Не определились с ответом"
        return self.choice_text