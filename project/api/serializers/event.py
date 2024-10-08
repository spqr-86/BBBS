from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, validators

from ..models import Event, Participant
from .tag import TagSerializer


class EventSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True)
    remain_seats = serializers.IntegerField(read_only=True)
    booked = serializers.BooleanField(read_only=True)

    class Meta:
        model = Event
        exclude = ['city', 'participants', 'seats']


class DateEventSerializer(serializers.Serializer):
    months = serializers.ListField(required=False, read_only=True)

    class Meta:
        fields = '__all__'


class ParticipantWriteSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    participant = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

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


class ParticipantReadSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = Participant
        fields = ['id', 'event']
