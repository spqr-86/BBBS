from rest_framework import serializers

from ..models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = History
