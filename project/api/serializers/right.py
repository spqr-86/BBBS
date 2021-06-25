from rest_framework import serializers

from ..models import Right
from .tag import TagSerializer


class RightSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)
    image = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        use_url=False
    )

    class Meta:
        fields = '__all__'
        model = Right
