from rest_framework import serializers

from ..models import Right, RightContent
from .tag import TagSerializer


class RightContentSerializer(serializers.ModelSerializer):
    text_blocks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='text',
    )

    class Meta:
        model = RightContent
        fields = ['block_type', 'title', 'text_blocks', 'colored_back']


class RightSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    content = RightContentSerializer(many=True, read_only=True)

    class Meta:
        model = Right
        fields = '__all__'


class RightListSerializer(RightSerializer):
    class Meta:
        model = Right
        fields = ['id', 'title', 'tags']
