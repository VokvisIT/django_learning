from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from .models import DataSet
from .forms import QuestForm
def polls_view(request: HttpRequest):
    if request.method == "POST":
        form = QuestForm(request.POST)
        if form.is_valid():
            DataSet.objects.create(**form.cleaned_data)
            url = reverse("questionnaire:result_list")
            return redirect(url)
    else:
        form = QuestForm()
    context = {
        "form": QuestForm()
    }
    return render(request, 'questionnaire/polls.html', context=context)

def result_view(request: HttpRequest):
    return render(request, 'questionnaire/result.html')