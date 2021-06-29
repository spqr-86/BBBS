from django_filters.filters import CharFilter
from django_filters.filterset import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Book
from ..serializers import BookSerializer


class TypeFilter(FilterSet):
    type = CharFilter(field_name='type__slug', method='filter_types')

    def filter_types(self, queryset, slug, types):
        return queryset.filter(type__slug__in=(types.split(',')))


class BookView(ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination
    filterset_backends = [DjangoFilterBackend]
    filter_class = TypeFilter
