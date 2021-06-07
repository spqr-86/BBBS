from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination

from ..models import Place
from ..serializers import PlaceSerializer


class PlacesViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin
):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        chosen = (serializer.validated_data['chosen']
                  or self.request.user.is_staff)
        serializer.save(
            chosen=chosen
        )
