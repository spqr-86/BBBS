from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Tag
from ..serializers import TagSerializer


class GetListPostPutMixin(
    GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin
):
    pass


class TagMixin:
    filterset_backends = [DjangoFilterBackend]
    filterset_fields = ['tags']

    @action(methods=['get'], detail=False)
    def tags(self, request):
        related_query_name = self.queryset.model._meta.get_field('tags') \
                                 .related_query_name()
        filter_key = f'{related_query_name}__isnull'
        tags = Tag.objects.filter(**{filter_key: False})
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
