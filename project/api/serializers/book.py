from ..models import Book
from .base import BaseSerializer


class BookSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Book
