from rest_framework import mixins, viewsets, permissions

from ..models import Place
from ..serializers import PlaceSerializer


class ListCreateDelViewSet(mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    pass


class PlaceViewSet(ListCreateDelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    search_fields = ['name']
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
