from rest_framework import serializers


class SearchResultSerializer(serializers.Serializer):
    title = serializers.CharField()
    model_name = serializers.CharField()
    rank = serializers.FloatField()
