from rest_framework import serializers

__all__ = (
    'QuestionSerializer',
    'Vote',
    'VoteResultsSerializer',
    'VoteResultsSerializer',
    'VoteSerializer',
)


class InnerChoiceListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    choice_text = serializers.CharField()


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question = serializers.CharField()
    choices = InnerChoiceListSerializer(many=True)


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
