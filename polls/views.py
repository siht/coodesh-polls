from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)

from .models import (
    Poll,
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
    queryset = Poll.objects.prefetch_related('choice_set')


class SubmitVoteView(CreateAPIView):
    '''submit a vote'''
    serializer_class = VoteSerializer


class VoteResultsView(RetrieveAPIView):
    '''get the clave for polls'''
    serializer_class = VoteResultsSerializer
