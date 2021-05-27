from rest_framework import permissions, viewsets

from ..models import Movie
from ..serializers import MovieSerializer


class MovieView(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None
