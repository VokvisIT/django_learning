from django import forms
from .models import DataSet

class QuestForm(forms.ModelForm):
    class Meta:
        model = DataSet
        fields = 'gender', 'open_question'
        widgets = {
            'gender': forms.RadioSelect(),
        }