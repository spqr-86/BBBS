from .base import BaseSerializer
from ..models import Article


class ArticleSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        tags = None
        model = Article
