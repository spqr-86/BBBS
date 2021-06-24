from django.utils.timezone import now
from rest_framework import serializers

from ..models import Diary


class DiarySerializer(serializers.ModelSerializer):
    mentor = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    date = serializers.DateField(default=now().date())
    image = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        use_url=False,
    )

    class Meta:
        fields = '__all__'
        model = Diary
