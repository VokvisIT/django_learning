from django.urls import path
from .views import polls_view, result_view
app_name = "questionnaire"
urlpatterns = [
    path("", polls_view, name="polls_view"),
    path("result/", result_view, name="result_view"),
]