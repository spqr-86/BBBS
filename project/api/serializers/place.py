from rest_framework import serializers

from ..models import Place
from .base import BaseSerializer


class PlaceSerializer(BaseSerializer):
    age_restriction = serializers.HiddenField(default='18')
    image = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        use_url=False,
        required=False,
    )

    class Meta(BaseSerializer.Meta):
        model = Place
