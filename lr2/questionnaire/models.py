from django.db import models
from django.db.models import Count

class Question(models.Model):
    QUESTION_TYPES = (
        ('open', 'Открытый вопрос'),
        ('single_choice', 'Одиночный выбор'),
        ('multiple_choice', 'Множественный выбор'),
    )
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

class Choice(models.Model):
    choice_text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    def __str__(self) -> str:
        return self.choice_text
    def get_statistics(self):
        return Answer.objects.filter(choice=self).aggregate(count=Count('id'))['count']

    def get_percentage(self):
        total_count = Answer.objects.filter(question=self.question).count()
        choice_count = Answer.objects.filter(question=self.question, choice=self).count()
        if total_count > 0:
            return round(choice_count / total_count * 100, 2)
        else:
            return 0

    @staticmethod
    def get_statistics_by_question(question_id):
        return Choice.objects.filter(question_id=question_id).annotate(count=Count('answer')).values('choice_text', 'count')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=255, null=True, blank=True)
    def get_percentage(self):
        total_count = Answer.objects.filter(question=self.question).count()
        choice_count = Answer.objects.filter(question=self.question, choice=self.choice).count()
        if total_count > 0:
            return round(choice_count / total_count * 100, 2)
        else:
            return 0