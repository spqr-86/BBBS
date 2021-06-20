from rest_framework import serializers

from ..models import Book
from .tag import TagSerializer


class BookSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
