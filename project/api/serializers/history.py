from rest_framework import serializers

from ..models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['output_to_main', ]
        model = History
