from rest_framework import serializers, validators
from django.utils.translation import gettext_lazy as _

from ..models import Event, Participant
from .tag import TagSerializer


class EventSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    taken_seats = serializers.IntegerField(read_only=True)
    booked = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = Event
        exclude = ['participants']


class ParticipantReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        exclude = ['participant']


class ParticipantWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Participant.objects.all(),
                fields=['event', 'participant'],
                message=_('Вы уже зарегестрированы на это событие')
            )
        ]