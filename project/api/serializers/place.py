from rest_framework import serializers

from ..models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Place
