from rest_framework import serializers

from ..models import Right
from .tag import TagSerializer


class RightSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)

    class Meta:
        fields = '__all__'
        model = Right
