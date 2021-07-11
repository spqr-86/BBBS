from rest_framework import serializers

from .booktype import BookTypeSerializer
from ..models import Book


class BookSerializer(serializers.ModelSerializer):
    type = BookTypeSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
