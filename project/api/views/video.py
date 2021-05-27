from rest_framework import permissions, viewsets

from ..models import Video
from ..serializers import VideoSerializer


class VideoView(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None
