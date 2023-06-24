from django import forms
from questionnaire.models import Choice, Question

class PollForm(forms.Form):
    def __init__(self, poll, *args, **kwargs):
        super().__init__(*args, **kwargs)
        questions = poll.question_set.all()
        for question in questions:
            if question.question_type == 'open':
                self.fields[f'question_{question.id}'] = forms.CharField(
                    label=question.question_text,
                    widget=forms.Textarea,
                    required=False  # Set the field as optional
                )
            elif question.question_type == 'multiple_choice':
                choices = question.choice_set.exclude(choice_text=None)
                self.fields[f'question_{question.id}'] = forms.MultipleChoiceField(
                    label=question.question_text,
                    choices=[(choice.id, choice.choice_text) for choice in choices],
                    widget=forms.CheckboxSelectMultiple,
                    required=False  # Set the field as optional
                )
            elif question.question_type == 'single_choice':
                choices = question.choice_set.exclude(choice_text=None)
                self.fields[f'question_{question.id}'] = forms.ChoiceField(
                    label=question.question_text,
                    choices=[(choice.id, choice.choice_text) for choice in choices],
                    widget=forms.RadioSelect,
                    required=False  # Set the field as optional
                )

    def save_answers(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('question_'):
                question_id = int(name.split('_')[1])
                question = Question.objects.get(id=question_id)
                if question.question_type == 'open':
                    if value:
                        existing_answer = Choice.objects.filter(question=question, choice_text=value).first()
                        if existing_answer:
                            existing_answer.answer_count += 1
                            existing_answer.save()
                        else:
                            Choice.objects.create(question=question, choice_text=value, answer_count=1)
                    else:
                        null_choice = question.choice_set.filter(choice_text=None).first()
                        if null_choice:
                            null_choice.answer_count += 1
                            null_choice.save()
                elif question.question_type in ['multiple_choice', 'single_choice']:
                    choices = question.choice_set.exclude(choice_text=None)
                    selected_choices = choices.filter(id__in=value)
                    for choice in selected_choices:
                        choice.answer_count += 1
                        choice.save()
                    if not selected_choices.exists():
                        null_choice = question.choice_set.filter(choice_text=None).first()
                        if null_choice:
                            null_choice.answer_count += 1
                            null_choice.save()

