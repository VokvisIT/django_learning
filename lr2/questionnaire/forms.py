from django import forms
from .models import Choice, Question, Answer, Poll

class SurveyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        questions = Question.objects.all()
        for question in questions:
            if question.question_type == 'single_choice':
                choices = [(choice.id, choice.choice_text) for choice in question.choice_set.all()]
                self.fields[f'question_{question.id}'] = forms.ChoiceField(label=question.question_text, choices=choices, widget=forms.RadioSelect)
            elif question.question_type == 'multiple_choice':
                choices = [(choice.id, choice.choice_text) for choice in question.choice_set.all()]
                self.fields[f'question_{question.id}'] = forms.MultipleChoiceField(label=question.question_text, choices=choices, widget=forms.CheckboxSelectMultiple)
            elif question.question_type == 'open':
                self.fields[f'question_{question.id}'] = forms.CharField(label=question.question_text, widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        for field_name, answer_data in cleaned_data.items():
            question_id = field_name.split('_')[-1]
            question = Question.objects.get(id=question_id)
            if question.question_type == 'open':
                answer = Answer(question=question, choice=None, answer_text=answer_data)
                answer.save()
            elif question.question_type == 'single_choice':
                choice = Choice.objects.get(id=answer_data)
                answer = Answer(question=question, choice=choice, answer_text=None)
                answer.save()
            elif question.question_type == 'multiple_choice':
                for choice_id in answer_data:
                    choice = Choice.objects.get(id=choice_id)
                    answer = Answer(question=question, choice=choice, answer_text=None)
                    answer.save()
        poll = Poll.objects.get(id=1)
        poll.count_comp_add()
        poll.save()
        
