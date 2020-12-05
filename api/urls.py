from django.urls import path, include
from rest_framework import routers
from . import views as api_views
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

"""
Dient dazu die URLs zu definieren bzw. zu der Logik mappen.
Es generiert automatisch die URLs und mappt die einzelnen endpoints zu den einzelnen viewsets, 
basirend auf den http-Typ (get, post, ...)
"""
routers = routers.DefaultRouter()
routers.register(r'provider', api_views.ProviderViewSet)
routers.register(r'place', api_views.PlaceViewSet)
routers.register(r'teacher', api_views.TeacherViewSet)
routers.register(r'student', api_views.StudentViewSet)
routers.register(r'course', api_views.CourseViewSet)
routers.register(r'users', api_views.UserViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(),name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'),name='swager-ui'),
    path('schema/redoc-ui/', SpectacularRedocView.as_view(url_name='schema'), name='redoc-ui'),

]