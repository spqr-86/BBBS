from rest_framework import serializers

from ..models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'booked', 'address', 'contact', 'title', 'description',
                  'start_at', 'end_at', 'seats', 'taken_seats', 'city')
        model = Event
