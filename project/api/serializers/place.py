from ..models import Place
from .base import BaseSerializer


class PlaceSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Place
