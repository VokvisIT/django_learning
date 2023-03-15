from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from timeit import default_timer
import timeit
def index(request: HttpRequest):
    context = {
        "time_running": round(timeit.timeit(), 5),
    }
    return render(request, 'firstapp/index.html', context=context)

def special(request: HttpRequest):
    context = {
        "time_running": round(timeit.timeit(), 5),
    }
    return render(request, 'firstapp/special.html', context=context)