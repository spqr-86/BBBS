from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Video
from ..serializers import VideoSerializer


class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
