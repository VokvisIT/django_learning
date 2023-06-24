from django.urls import path
from .views import list_qest, polls_view, result_view
app_name = "questionnaire"
urlpatterns = [
    path("", list_qest, name="list_qest"),
    path("poll/<int:poll_id>/", polls_view, name="polls_view"),
    path("result/<int:poll_id>/", result_view, name="result_view"),
]