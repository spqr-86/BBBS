from requests.exceptions import RequestException

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import status, views
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ..serializers import EmailSerializer, ProfileSerializer
from ..utils.email import send_email

User = get_user_model()


class ProfileViewSet(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class SendPassView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = request.data.get('email')
            if not User.objects.filter(email=email).exists():
                message = {
                    'email': _(
                        'Пользователь с таким email не зарегестрирован.'
                    )
                }
                return Response(message, status=status.HTTP_200_OK)
            try:
                send_email(email, 'password', 'Тут будет ссылка.')
            except RequestException:
                message = {
                    'email': _('Проблемы с отправкой, попробуйте позднее.')
                }
                return Response(
                    message,
                    status=status.HTTP_504_GATEWAY_TIMEOUT
                )
            message = {
                'email': _(
                    f'Ссылка для сброса пароля была отправлена на {email}.'
                )
            }
            return Response(message, status=status.HTTP_200_OK)
