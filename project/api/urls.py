from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import *  # noqa F405

v1_router = DefaultRouter()

v1_router.register(r'articles', ArticleViewSet, basename='article')
v1_router.register(r'history', HistoryViewSet, basename='history')
v1_router.register(r'places', PlaceViewSet, basename='place')
v1_router.register(r'tags', TagViewSet, basename='tag')
v1_router.register(r'movies', MovieView, basename='movies')
v1_router.register(r'videos', VideoView, basename='videos')
v1_router.register(r'questions', QuestionViewSet, basename='questions')
v1_router.register(r'cityes', CityViewSet, basename='cityes')
v1_router.register(r'events', EventViewSet, basename='events')

app_name = 'api'

urlpatterns = [
    path('v1/token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/', include(v1_router.urls)),
]
