from ..models import Movie
from .base import BaseSerializer


class MovieSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Movie
