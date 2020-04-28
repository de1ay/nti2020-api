from django.contrib.auth.views import LogoutView
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from . import views


router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet, basename='message')


urlpatterns = [
    url(r'^', include(router.urls)),
    path('messages/user/<int:target_id>/', views.MessageViewSet.as_view({"get": "user"})),
]
