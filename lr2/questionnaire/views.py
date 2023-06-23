
from django.shortcuts import redirect, render
from django.http import HttpRequest

from questionnaire.forms import SurveyForm
from questionnaire.models import Poll, Question

def polls_view(request: HttpRequest):
    context = {
    }
    return render(request, 'questionnaire/polls.html', context=context)

def result_view(request):
    context = {
    }
    return render(request, 'questionnaire/result.html', context=context)