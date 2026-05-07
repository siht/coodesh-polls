from collections import defaultdict

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response


from .models import (
    Poll,
)
from .serializers import (
    QuestionListSerializer,
    QuestionCreateSerializer,
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
    serializer_class = defaultdict(
        lambda: QuestionListSerializer,
        {
            'post': QuestionCreateSerializer,
        }
    )
    
    queryset = Poll.objects.prefetch_related('choice_set')

    def get_serializer_class(self, key=None):
        if key:
            return self.serializer_class[key]
        return self.serializer_class[self.request.method.lower()]

    def get_serializer(self, *args, **kwargs):
        key = None
        if 'key' in kwargs:
            key = kwargs.pop('key')
        if key:
            serializer_class = self.get_serializer_class(key=key)
        else:
            serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        key=f'output_{self.request.method.lower()}'
        if key in self.serializer_class.keys():
            serializer = self.get_serializer(instance, key=key)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SubmitVoteView(CreateAPIView):
    '''submit a vote'''
    serializer_class = VoteSerializer


class VoteResultsView(RetrieveAPIView):
    '''get the clave for polls'''
    serializer_class = VoteResultsSerializer
    queryset = Poll.objects.all()
    lookup_field = 'id'
