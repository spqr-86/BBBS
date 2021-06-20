from django.utils.timezone import now
from rest_framework import serializers

from ..models import Diary


class DiarySerializer(serializers.ModelSerializer):
    mentor = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    date = serializers.DateField(default=now().date())

    class Meta:
        fields = '__all__'
        model = Diary
