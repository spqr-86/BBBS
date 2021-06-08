from rest_framework import serializers

from ..models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['output_to_main', ]
        model = Article
