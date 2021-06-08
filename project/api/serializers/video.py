from rest_framework import serializers

from ..models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['output_to_main', ]
        model = Video
