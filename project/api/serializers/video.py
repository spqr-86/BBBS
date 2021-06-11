from ..models import Video
from .base import BaseSerializer


class VideoSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Video
