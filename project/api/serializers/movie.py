from .base import BaseSerializer
from ..models import Movie


class MovieSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Movie
