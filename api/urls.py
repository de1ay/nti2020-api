from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users-info', views.UserInfoViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('users-info/user/<int:target_id>/', views.UserInfoViewSet.as_view({"get": "user"})),
    path('push-subscribe', views.subscribe),
]
