
from django.shortcuts import redirect, render
from django.http import HttpRequest

from questionnaire.forms import SurveyForm
from questionnaire.models import Poll, Question

def polls_view(request: HttpRequest):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            return redirect('questionnaire:result_view')

    else:
        form = SurveyForm()
    context = {
        'form': form,
    }
    return render(request, 'questionnaire/polls.html', context=context)

def result_view(request):
    context = {
        'count': Poll.objects.get(id=1),
        'questions': Question.objects.all(),
    }
    return render(request, 'questionnaire/result.html', context=context)