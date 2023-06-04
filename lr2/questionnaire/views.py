
from django.shortcuts import redirect, render
from django.http import HttpRequest

from questionnaire.forms import SurveyForm

def polls_view(request: HttpRequest):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            return redirect('questionnaire:result_view')
        else:
            # Print the errors to the console for debugging
            print("===========================")
            print(form.errors)
            print("===========================")
    else:
        form = SurveyForm()
    context = {
        'form': form,
    }
    return render(request, 'questionnaire/polls.html', context=context)

def result_view(request: HttpRequest):
    return render(request, 'questionnaire/result.html')