from rest_framework import permissions, viewsets

from ..models import Article
from ..serializers import ArticleSerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
