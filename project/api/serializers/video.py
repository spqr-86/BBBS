from .base import BaseSerializer
from ..models import Video


class VideoSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        tags = None
        model = Video
