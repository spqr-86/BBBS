from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Movie
from ..serializers import MovieSerializer
from . import TagMixin


class MovieView(ReadOnlyModelViewSet, TagMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
