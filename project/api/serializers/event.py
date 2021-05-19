from rest_framework import serializers

from ..models import Event
from .tag import TagSerializer


class EventSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)
    taken_seats = serializers.IntegerField(read_only=True)
    booked = serializers.BooleanField(read_only=True)

    class Meta:
        exclude = ['participant']
        model = Event
