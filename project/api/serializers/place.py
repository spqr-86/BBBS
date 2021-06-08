from rest_framework import serializers

from ..models import Place
from .tag import TagSerializer


class PlaceSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)

    class Meta:
        exclude = ['output_to_main', ]
        model = Place
