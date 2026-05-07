from rest_framework.generics import ListCreateAPIView
from .serializers import QuestionSerializer

__all__ = (
    'QuestionCreateListAPIView',
)

class QuestionCreateListAPIView(ListCreateAPIView):
    '''creation and list Polls'''
    serializer_class = QuestionSerializer
