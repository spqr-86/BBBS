from rest_framework import serializers

from ..models import Event
from .tag import TagSerializer


class EventSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)

    class Meta:
        fields = '__all__'
        model = Event
