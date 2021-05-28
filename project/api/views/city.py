<<<<<<< HEAD
from rest_framework import permissions, viewsets
=======
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
>>>>>>> main

from ..models import City
from ..serializers import CitySerializer


<<<<<<< HEAD
class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all().order_by('-is_primary')
    serializer_class = CitySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
=======
class CityViewSet(ReadOnlyModelViewSet):
    queryset = City.objects.all().order_by('-is_primary')
    serializer_class = CitySerializer
    permission_classes = [AllowAny]
    pagination_class = None
>>>>>>> main
