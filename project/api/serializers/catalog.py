from rest_framework import serializers

from ..models import Catalog


class CatalogSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        use_url=False
    )
    
    class Meta:
        model = Catalog
        fields = '__all__'
