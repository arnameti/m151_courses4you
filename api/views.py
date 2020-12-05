from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ProviderSerializer, PlaceSerializer, TeacherSerializer, StudentSerializer, \
    CourseSerializer, UserSerializer
from .models import Provider, Place, Teacher, Student, Course
from django.contrib.auth.models import User
from .permissions import IsAuthenticatedOrPostOnly
from drf_spectacular.utils import extend_schema

# Create your views here.
"""
Django stellt die Klasse Viewsets zur Verfügung, um die Logik für die APIs zu erstellen.
Mit Viewsets kann man die Logik für die Endpoints definieren.(get, post, put, patch, delete)
Man muss vieles importieren. Dies ist am Anfang der Datei ersichtich. Was erwähnenswert ist die Importierung von viewsets und permissions.
Dazu muss vorher das django rest_framework installiert werden.
permission_classes = [permissions.IsAuthenticatedOrReadOnly] --> bedeutet, dass die Daten ausgelesen werden können,
aber um einen Provider zu erstellen, löschen oder bearbeiten, muss man sich vorher authentifizieren.
"""
@extend_schema(tags=['Provider'])
class ProviderViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

# Viewset für Place
@extend_schema(tags=['Place'])
class PlaceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

# Viewset für Teacher
@extend_schema(tags=['Teacher'])
class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# Viewset für Student
@extend_schema(tags=['Student'])
class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Viewset für Course
@extend_schema(tags=['Course'])
class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Viewset für User
@extend_schema(tags=['User'])
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrPostOnly]

    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer