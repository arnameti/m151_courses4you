from django.urls import path, include
from rest_framework import routers
from . import views as api_views

routers = routers.DefaultRouter()
routers.register(r'anbieter', api_views.AnbieterViewSet)
routers.register(r'anschrift', api_views.AnschriftViewSet)
routers.register(r'kursleiter', api_views.KursleiterViewSet)
routers.register(r'kursteilnehmer', api_views.KursteilnehmerViewSet)
routers.register(r'kurs', api_views.KursViewSet)


urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth', include('rest_framework.urls')),
]