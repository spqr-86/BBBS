from rest_framework import serializers

from ..models import Place
from .base import BaseSerializer


class PlaceSerializer(BaseSerializer):
    image = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        use_url=False
    )

    class Meta(BaseSerializer.Meta):
        model = Place
