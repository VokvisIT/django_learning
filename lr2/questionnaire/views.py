from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse, reverse_lazy

from questionnaire.models import Choice, Question

from .forms import SurveyForm

def polls_view(request: HttpRequest):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            for question in form.fields:
                answer = form.cleaned_data[question]
                if answer:
                    answer_obj = form.save(commit=False)
                    answer_obj.question_id = question.split('_')[1]
                    if isinstance(answer, list):
                        answer_obj.text = ', '.join([str(a) for a in answer])
                    elif isinstance(answer, str):
                        answer_obj.text = answer
                    else:
                        answer_obj.choice_id = answer.id
                    answer_obj.save()
            url = reverse("questionnaire:result_list")
            return redirect(url)
    else:
        form = SurveyForm()
    context = {
        "form": SurveyForm()
    }
    return render(request, 'questionnaire/polls.html', context=context)

def result_view(request: HttpRequest):
    questions = Question.objects.all()
    statistics = {}
    for question in questions:
        statistics[question.id] = Choice.get_statistics_by_question(question.id)
    return render(request, 'questionnaire/result.html', {'questions': questions, 'statistics': statistics})