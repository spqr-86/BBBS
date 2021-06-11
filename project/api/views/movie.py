from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import TagMixin
from ..models import Movie
from ..serializers import MovieSerializer


class MovieView(ReadOnlyModelViewSet, TagMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
