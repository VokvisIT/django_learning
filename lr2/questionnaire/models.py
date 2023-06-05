from django.db import models
from django.db.models import Count

QUESTION_TYPES = (
        ('single_choice', 'Одиночный выбор'),
        ('multiple_choice', 'Множественный выбор'),
        ('open', 'Открытый вопрос'),
    )

class Question(models.Model):
    question_text = models.CharField(max_length=255, null=True, blank=True)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    num_answers = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text.title()
    def get_answers_data(self):
        if self.question_type == 'open':
            answers = self.answer_set.all().values('answer_text')
            answer_counts = answers.annotate(count=Count('answer_text')).order_by('answer_text')
            total_count = self.num_answers
            answer_data = []
            for answer_count in answer_counts:
                answer_text = answer_count['answer_text']
                count = answer_count['count']
                percentage = count / total_count * 100 if total_count > 0 else 0
                answer_data.append({
                    'answer_text': answer_text,
                    'count': count,
                    'percentage': percentage,
                })
        else:
            answers = self.answer_set.all().select_related('choice')
            answer_counts = answers.values('choice__choice_text').annotate(count=Count('id'))
            total_count = self.num_answers
            answer_data = []
            for answer_count in answer_counts:
                answer_text = answer_count['choice__choice_text']
                count = answer_count['count']
                percentage = count / total_count * 100 if total_count > 0 else 0
                answer_data.append({
                    'answer_text': answer_text,
                    'count': count,
                    'percentage': percentage,
                })
        return answer_data

class Choice(models.Model):
    """Класс для набора разных вариантов ответа на single_choice и multiple_choice"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.choice_text.title()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    answer_text = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice or self.answer_text}'
    def save(self, *args, **kwargs):
            if self.choice:
                self.question.num_answers += 1
                self.question.save()
            super().save(*args, **kwargs)