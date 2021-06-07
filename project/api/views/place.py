from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Place, Tag
from ..serializers import PlaceSerializer
from .tag import TagSerializer


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
    filterset_backends = [DjangoFilterBackend]
    filterset_fields = ['tags']

    @action(methods=['get'], detail=False)
    def tags(self, request):
        tags = Tag.objects.filter(places__isnull=False)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        chosen = (serializer.validated_data['chosen']
                  or self.request.user.is_staff)
        serializer.save(
            chosen=chosen
        )
