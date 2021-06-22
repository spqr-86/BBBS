from rest_framework import permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from ..models import Diary
from ..serializers import DiarySerializer
from ..permissions import IsOwner


class DiaryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = DiarySerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Diary.objects.filter(mentor=self.request.user)

    def perform_create(self, serializer):
        serializer.save(mentor=self.request.user)
