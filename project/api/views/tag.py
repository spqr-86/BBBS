from rest_framework import mixins, permissions, viewsets

from ..models import Tag
from ..serializers import TagSerializer


class ListCreateDelViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    pass


class TagViewSet(ListCreateDelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'
    search_fields = ['name']
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
