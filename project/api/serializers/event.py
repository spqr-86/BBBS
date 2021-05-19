from rest_framework import serializers

from ..models import Event
from .tag import TagSerializer


class EventSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)
    taken_seats = serializers.IntegerField(read_only=True)
    booked = serializers.SerializerMethodField()

    class Meta:
        exclude = ['participant']
        model = Event

    def get_booked(self, obj):
        return Event.objects.filter(participant=self.context['user']).exists()
