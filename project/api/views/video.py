from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Video
from ..serializers import VideoSerializer
from . import TagMixin


class VideoView(ReadOnlyModelViewSet, TagMixin):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination
