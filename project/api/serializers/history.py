from rest_framework import validators
from rest_framework.serializers import CurrentUserDefault

from .base import BaseSerializer
from .profile import MentorSerializer
from ..models import History


class HistorySerializer(BaseSerializer):
    mentor = MentorSerializer(default=CurrentUserDefault())

    class Meta(BaseSerializer.Meta):
        tags = None
        model = History
        validators = [
            validators.UniqueTogetherValidator(
                queryset=History.objects.all(),
                fields=['mentor', 'child'],
                message='Такая пара наставник - ребенок уже добавлена'
            )
        ]
