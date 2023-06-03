from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'choice', 'answer_text']
        widgets = {
            'question': forms.HiddenInput(),
            'choice': forms.CheckboxInput(attrs={'required': False}),
            'answer_text': forms.TextInput(attrs={'required': False}),
        }

    def save(self, commit=True):
        answer = super().save(commit=False)
        if answer.question.question_type == 'multiple_choice':
            choices = self.cleaned_data.getlist('choice')
            for choice in choices:
                answer.pk = None
                answer.choice = choice
                answer.answer_text = None
                if commit:
                    answer.save()
        else:
            if commit:
                answer.save()
        return answer
    def clean_choice(self):
        choices = self.cleaned_data['choice']
        if not choices:
            raise forms.ValidationError('At least one choice must be selected.')
        return choices


