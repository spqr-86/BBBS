from ..models import Article
from .base import BaseSerializer


class ArticleSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        tags = None
        model = Article
