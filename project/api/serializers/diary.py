from ..models import Diary
from .base import BaseSerializer


class DiarySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Diary
