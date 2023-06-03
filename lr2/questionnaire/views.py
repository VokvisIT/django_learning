from django.shortcuts import render
from django.http import HttpRequest

def polls_view(request: HttpRequest):
    context = {}
    return render(request, 'questionnaire/polls.html', context)

def result_view(request: HttpRequest):
    return render(request, 'questionnaire/result.html')