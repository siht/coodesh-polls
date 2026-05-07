from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
)
from .serializers import (
    QuestionSerializer,
    VoteSerializer,
)

__all__ = (
    'QuestionCreateListAPIView',
)

class QuestionCreateListAPIView(ListCreateAPIView):
    '''creation and list Polls'''
    serializer_class = QuestionSerializer


class VoteView(CreateAPIView):
    serializer_class = VoteSerializer

