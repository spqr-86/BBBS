from .base import BaseSerializer
from ..models import History


class HistorySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        tags = None
        model = History
