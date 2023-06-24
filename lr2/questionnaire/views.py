
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from questionnaire.forms import PollForm

from questionnaire.models import Poll

def list_qest(request: HttpRequest):
    context = {
        'polls': Poll.objects.all()
    }
    return render(request, 'questionnaire/listQest.html', context=context)

def polls_view(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        form = PollForm(poll, request.POST)
        if form.is_valid():
            form.save_answers()
            return redirect('questionnaire:result_view', poll_id=poll_id)
    else:
        form = PollForm(poll)
    context = {
        'poll': poll,
        'form': form
    }
    return render(request, 'questionnaire/polls.html', context=context)

def result_view(request: HttpRequest, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    questions = poll.question_set.all()
    context = {
        'poll': poll,
        'questions': questions
    }
    return render(request, 'questionnaire/result.html', context=context)