from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)
from .serializers import (
    QuestionSerializer,
    VoteSerializer,
    VoteResultsSerializer,
)

__all__ = (
    'QuestionCreateListAPIView',
    'SubmitVoteView',
    'VoteResultsView',
)

class QuestionCreateListAPIView(ListCreateAPIView):
    '''creation and list Polls'''
    serializer_class = QuestionSerializer


class SubmitVoteView(CreateAPIView):
    serializer_class = VoteSerializer


class VoteResultsView(RetrieveAPIView):
    serializer_class = VoteResultsSerializer
