from django.urls import reverse
from rest_framework import serializers

from ..models import Right
from .tag import TagSerializer


class RightNextSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Right
        fields = ['id', 'title', 'url']

    def get_url(self, obj):
        return reverse(
            f'api:v1:{obj.__class__.__name__.lower()}-detail',
            kwargs={'pk': obj.id}
        )


class RightSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)
    next_article = serializers.SerializerMethodField()

    class Meta:
        model = Right
        fields = '__all__'

    def get_next_article(self, obj):
        queryset = Right.objects.filter(id__lt=obj.id)
        tags = self.context['request'].query_params.get('tags')
        if tags is not None:
            queryset = queryset.filter(tags__slug__in=tags.split(','))
        if not queryset.exists():
            return None
        serializer = RightNextSerializer(queryset.first())
        return serializer.data


class RightListSerializer(RightSerializer):
    class Meta(RightSerializer.Meta):
        model = Right
        fields = ['id', 'title', 'tags']
