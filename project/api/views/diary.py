from django.utils.translation import gettext_lazy as _
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from ..models import Diary
from ..permissions import IsOwner
from ..serializers import DiarySerializer


class DiaryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = DiarySerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Diary.objects.filter(mentor=self.request.user)

    def perform_create(self, serializer):
        serializer.save(mentor=self.request.user)

    @action(methods=['post'], detail=True)
    def send(self, request, pk=None):
        diary = get_object_or_404(Diary, pk=pk, mentor=request.user)
        if not diary.sent_to_curator:
            diary.sent_to_curator = True
            diary.save()
            message = {'diary': _('Запись дневника отправлена куратору.')}
            return Response(message, status=status.HTTP_200_OK)
        message = {'diary': _('Запись дневника уже была отправлена куратору.')}
        return Response(message, status=status.HTTP_200_OK)
