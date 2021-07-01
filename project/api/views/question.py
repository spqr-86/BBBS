from django_filters.filters import CharFilter
from django_filters.filterset import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from ..models import Question, Tag
from ..serializers import QuestionSerializer, TagSerializer
from . import GetListPostPutMixin


class TagsFilter(FilterSet):
    tags = CharFilter(field_name='tags__slug', method='filter_tags')

    def filter_tags(self, queryset, slug, tags):
        return queryset.filter(tags__slug__in=(tags.split(',')))


class QuestionViewSet(GetListPostPutMixin):
    queryset = Question.objects.exclude(answer=None)
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination
    filterset_backends = [DjangoFilterBackend]
    filter_class = TagsFilter

    @action(methods=['get'], detail=False)
    def tags(self, request):
        queryset = self.get_queryset()
        tags = Tag.objects.filter(questions__in=queryset).distinct()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
