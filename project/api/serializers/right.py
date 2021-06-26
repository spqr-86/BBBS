from rest_framework import serializers

from ..models import Right
from .tag import TagSerializer


class RightListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)

    class Meta:
        fields = ['id', 'title', 'tags']
        model = Right


class RightRetrieveSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)

    class Meta:
        fields = '__all__'
        model = Right
