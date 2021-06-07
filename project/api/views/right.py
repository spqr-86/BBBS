from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Right, Tag
from ..serializers import RightSerializer, TagSerializer


class RightViewSet(ReadOnlyModelViewSet):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

    @action(methods=['get'], detail=False)
    def tags(self, request):
        tags_id = Right.objects.values_list('tags', flat=True)
        tags = Tag.objects.filter(pk__in=tags_id)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
