from django.db import transaction
from rest_framework import serializers

from .models import (
    Choice,
    Poll,
)

__all__ = (
    'QuestionCreateSerializer',
    'QuestionListSerializer',
    'Vote',
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


class InnerChoiceSerializer(serializers.Serializer):
    question = serializers.CharField()
    votes = serializers.IntegerField()


class VoteResultsSerializer(serializers.Serializer):
    question = serializers.CharField()
    total_votes = serializers.IntegerField()
    choices = InnerChoiceSerializer(many=True)


class Vote(serializers.Serializer):
    choice_id = serializers.IntegerField()
