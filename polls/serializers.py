from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from django.db import transaction
from rest_framework import serializers

from .models import (
    Choice,
    Poll,
    Vote,
)

__all__ = (
    'QuestionCreateSerializer',
    'QuestionListSerializer',
    'VoteResultsSerializer',
    'VoteSerializer',
)


class InnerChoiceListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Choice
        fields = ('id', 'text')


class QuestionListSerializer(serializers.ModelSerializer):
    choices = InnerChoiceListSerializer(many=True, source='choice_set', allow_empty=False, allow_null=False)

    class Meta:
        model = Poll
        fields = ('id', 'question', 'choices')


class QuestionCreateSerializer(serializers.ModelSerializer):
    choices = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = Poll
        fields = ('question', 'choices')


    def validate(self, attrs):
        choices = attrs.get('choices')
        if choices and len(choices) < 2:
            raise serializers.ValidationError("At least two choices are required.")
        return attrs

    @transaction.atomic
    def save(self, **kwargs):
        choices_list = self.validated_data.pop('choices')
        poll = super().save(**kwargs)
        for choice_text in choices_list:
            Choice.objects.create(poll=poll, text=choice_text)
        return poll


class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()

    def validate_choice_id(self, value):
        if not Choice.objects.filter(id=value).exists():
            raise serializers.ValidationError(f"Choice with id {value} does not exist.")
        return value

    def save(self, **kwargs):
        choice_id = self.validated_data['choice_id']
        vote = Vote.objects.create(choice_id=choice_id)
        return vote


class InnerChoiceSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='text')
    votes = serializers.IntegerField()

    class Meta:
        model = Choice
        fields = ('question', 'votes')


class VoteResultsSerializer(serializers.ModelSerializer):
    total_votes = serializers.IntegerField()
    choices = InnerChoiceSerializer(many=True, source='choice_set')

    class Meta:
        model = Poll
        fields = ('id', 'question', 'total_votes', 'choices', 'total_votes')
