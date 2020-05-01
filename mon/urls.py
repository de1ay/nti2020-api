from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'record', views.RecordViewSet)
router.register(r'receive', views.ReceiveNotifications)


urlpatterns = [
    url(r'^', include(router.urls)),
]
