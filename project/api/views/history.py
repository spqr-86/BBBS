from rest_framework import permissions, viewsets

from ..models import History
from ..serializers import HistorySerializer


class HistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
