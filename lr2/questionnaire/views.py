from django.shortcuts import redirect, render
from django.http import HttpRequest

from questionnaire.forms import QuestionForm
from questionnaire.models import Question

def polls_view(request: HttpRequest):
    form = QuestionForm(request.POST)
    if request.method == 'POST':
        # print(request.POST)  # добавленная инструкция print
        # <QueryDict: {'csrfmiddlewaretoken': ['NrWOVJYYWQSyBTCYJmLZEBeGMjuWXbcIU81cOSSYII11NI3xthvwqnh7ULw3lZSR'], 'answer_text': ['324234', '23424'], 'choice': ['7', '3', '4']}>
        print(request.POST.getlist('choice'))
        if form.is_valid():
            form.save()
            return redirect('result_view')

    questions = Question.objects.all()
    context = {
        'form': form,
        'questions': questions,
    }
    return render(request, 'questionnaire/polls.html', context=context)

def result_view(request: HttpRequest):
    return render(request, 'questionnaire/result.html')