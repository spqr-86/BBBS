from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Right
from ..serializers import RightSerializer

from . import TagMixin


class RightViewSet(ReadOnlyModelViewSet, TagMixin):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
