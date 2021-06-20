from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination

from ..filters import PlaceFilter
from ..models import Place
from ..serializers import PlaceSerializer
from .mixins import GetListPostPutMixin, TagMixin


class PlacesViewSet(GetListPostPutMixin, TagMixin):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_class = PlaceFilter

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
