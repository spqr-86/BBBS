from django.urls import reverse
from rest_framework import serializers

from ..models import Catalog


class CatalogNextSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Catalog
        exclude = ['description', 'image', 'image_url', 'body']

    def get_url(self, obj):
        return reverse(
            f'api:v1:{obj.__class__.__name__.lower()}-detail',
            kwargs={'pk': obj.id}
        )


class CatalogSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        use_url=False,
        required=False,
    )
    next_article = serializers.SerializerMethodField()

    class Meta:
        model = Catalog
        exclude = ['image_url']

    def get_next_article(self, obj):
        queryset = Catalog.objects.filter(id__lt=obj.id)
        if not queryset.exists():
            return None
        serializer = CatalogNextSerializer(queryset.first())
        return serializer.data


class CatalogListSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        use_url=False,
        required=False,
    )

    class Meta:
        model = Catalog
        exclude = ['description', 'image_url', 'body']
