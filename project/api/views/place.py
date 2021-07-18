from http import HTTPStatus

from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from ..filters import PlaceFilter
from ..models import Place
from ..serializers import PlaceSerializer, TagSerializer
from .mixins import GetListPostPutMixin
from ..utils.tag_filtrator import tags_by_city_filter


class PlacesViewSet(GetListPostPutMixin):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_class = PlaceFilter

    @action(methods=['get'], detail=False)
    def tags(self, request):
        if self.request.user is None:
            return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        if self.request.user.is_authenticated:
            tags = tags_by_city_filter(self.request)
            serializer = TagSerializer(tags, many=True)
            return Response(serializer.data)
        return tags_by_city_filter(self.request)

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        if user.is_authenticated:
            return queryset.filter(city=user.city)
        city = self.request.data.get('city')
        if city is not None:
            return queryset.filter(city=city)
        return queryset

    def perform_create(self, serializer):
        serializer.save(chosen=self.request.user.is_mentor)