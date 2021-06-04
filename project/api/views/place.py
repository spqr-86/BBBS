from rest_framework import mixins, permissions, viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination

from ..models import Place
from ..serializers import PlaceSerializer


class PlaceViewSet(
    GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.AllowAny]


class PlacesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberPagination
