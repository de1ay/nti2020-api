from django.contrib.auth.views import LogoutView
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from . import views


router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet, basename='message')
router.register(r'chat-group', views.ChatGroupViewSet, basename='chat-group')
router.register(r'chat-users', views.ChatUsersViewSet, basename='chat-users')
router.register(r'chat-message', views.ChatMessageViewSet, basename='chat-message')


urlpatterns = [
    url(r'^', include(router.urls)),
    path('messages/user/<int:target_id>/', views.MessageViewSet.as_view({"get": "user"})),
]
