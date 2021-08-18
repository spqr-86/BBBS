from django_filters.filters import CharFilter
from django_filters.filterset import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Book, BookType
from ..serializers import (BookSerializer, BookResponseSerializer,
                           BookTypeSerializer)

SORTED_QUERY = ('select '
                'rank() over (partition by b.type_id order by b.id desc), b.* '
                'from  api_book b '
                'order by 1, 2 desc '
                'limit {limit} offset {offset};')


URL_TEMPLATE = '{path}?limit={limit}&offset={offset}'

DEFAULT_LIMIT = settings.REST_FRAMEWORK.get('PAGE_SIZE', '10')


class TypeFilter(FilterSet):
    types = CharFilter(field_name='type__slug', method='filter_types')

    def filter_types(self, queryset, slug, types):
        return queryset.filter(type__slug__in=(types.split(',')))


class BookList:
    count = 0
    next = None
    previous = None
    results = None


class BookView(ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination
    filterset_backends = [DjangoFilterBackend]
    filter_class = TypeFilter

    def list(self, request, *args, **kwargs):
        limit = int(request.GET.get('limit', DEFAULT_LIMIT))
        offset = int(request.GET.get('offset', '0'))  # int-защита от инъекции
        next = None
        path = request.path
        previous = None
        if offset:
            previous = URL_TEMPLATE.format(
                path=path,
                limit=limit,
                offset=offset - limit
            )
        queryset = Book.objects.raw(
            SORTED_QUERY.format(limit=limit, offset=offset)
        )
        count = Book.objects.count()
        if limit + offset < count:
            next = URL_TEMPLATE.format(
                path=path,
                limit=limit,
                offset=offset + DEFAULT_LIMIT
            )
        serializer = BookResponseSerializer(BookList)
        serializer.instance.count = count
        serializer.instance.previous = previous
        serializer.instance.next = next
        serializer.instance.results = queryset
        return Response(data=serializer.data)

    @action(methods=['get'], detail=False)
    def types(self, request):
        related_query_name = self.queryset.model._meta.get_field(
            'type'
        ).related_query_name()
        filter_key = f'{related_query_name}__in'
        types = BookType.objects.filter(
            **{filter_key: self.queryset}
        ).distinct()
        serializer = BookTypeSerializer(types, many=True)
        return Response(serializer.data)
