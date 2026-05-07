from django.urls import path
from .views import QuestionCreateListAPIView

urlpatterns = [
    path('', QuestionCreateListAPIView.as_view(), name='create-list-poll'),
]
