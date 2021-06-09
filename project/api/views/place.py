from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

from ..models import Place
from ..serializers import PlaceSerializer
from . import GetListPostPutMixin, TagMixin


class PlacesViewSet(GetListPostPutMixin, TagMixin):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(chosen=self.request.user.is_mentor)
