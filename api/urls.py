from django.conf.urls import url, include
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
router = DefaultRouter()
router.register(r'structures', StructuresViewSet)
router.register(r'terminals', TerminalViewSet)
router.register(r'events', EventsViewSet)
router.register(r'play_list_advertisements', PlayListAdvertisingViewSet)
urlpatterns += router.urls
