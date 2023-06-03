from django import forms
from .models import Question, Answer

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for question in Question.objects.all():
            if question.question_type == 'open':
                self.fields[f'question_{question.id}'] = forms.CharField(label=question.question_text, required=False)
            elif question.question_type == 'single_choice':
                self.fields[f'question_{question.id}'] = forms.ModelChoiceField(label=question.question_text, queryset=question.choice_set.all(), empty_label=None, widget=forms.RadioSelect)
            elif question.question_type == 'multiple_choice':
                self.fields[f'question_{question.id}'] = forms.ModelMultipleChoiceField(label=question.question_text, queryset=question.choice_set.all(), widget=forms.CheckboxSelectMultiple)
