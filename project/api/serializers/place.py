from django.utils.translation import gettext_lazy as _
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

    def validate_age(self, value):
        if value > 25:
            raise serializers.ValidationError(
                _('Слишком большой возраст для ребёнка')
            )
        elif value < 8:
            raise serializers.ValidationError(
                _('Возраст не может быть меньше 0')
            )
        return value
