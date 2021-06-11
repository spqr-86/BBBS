from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import TagMixin
from ..models import Video
from ..serializers import VideoSerializer


class VideoView(ReadOnlyModelViewSet, TagMixin):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
