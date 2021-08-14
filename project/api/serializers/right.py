from rest_framework import serializers

from ..models import Right
from .tag import TagSerializer


class RightSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Right
        fields = '__all__'


class RightListSerializer(RightSerializer):
    class Meta(RightSerializer.Meta):
        model = Right
        fields = ['id', 'title', 'tags']
