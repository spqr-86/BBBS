from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *  # noqa F405

v1_router = DefaultRouter()

v1_router.register(r'articles', ArticleViewSet, basename='article')
v1_router.register(r'history', HistoryViewSet, basename='history')
v1_router.register(r'questions', QuestionViewSet, basename='questions')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
