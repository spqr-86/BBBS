from rest_framework import serializers

from ..models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'info', 'link', 'image_url', 'duration')
