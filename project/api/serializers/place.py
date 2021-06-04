from rest_framework import serializers

from ..models import Place


class PlaceSerializer(serializers.ModelSerializer):
    choosen = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        exclude = ['city']
        model = Place
