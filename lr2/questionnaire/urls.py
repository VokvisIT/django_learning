from django.urls import path
from .views import polls_view, result_view
app_name = "questionnaire"
urlpatterns = [
    path("polls/", polls_view, name="polls_list"),
    path("result/", result_view, name="result_list"),
]