from rest_framework import permissions, viewsets
from rest_framework.pagination import PageNumberPagination

from ..models import Place
from ..serializers import PlaceSerializer


class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberPagination
