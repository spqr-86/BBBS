from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

from .mixins import GetListPostPutMixin
from ..models import History
from ..serializers import HistorySerializer


class HistoryViewSet(GetListPostPutMixin):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
