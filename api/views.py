from rest_framework import viewsets, permissions
from .serializers import ProviderSerializer, PlaceSerializer, TeacherSerializer, StudentSerializer, \
    CourseSerializer, UserSerializer
from .models import Provider, Place, Teacher, Student, Course
from django.contrib.auth.models import User
from .permissions import IsAuthenticatedOrPostOnly
from drf_spectacular.utils import extend_schema

# Create your views here.

@extend_schema(tags=['Provider'])
class ProviderViewSet(viewsets.ModelViewSet):
    """
    Ein Viewset  für "Web Request" und "Web Response"
    Enthält die ganze nötige Logik um Requests zu bearbeiten.
    Für Änderungen durch den User, ist eine Authentifizierung nötig.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


@extend_schema(tags=['Place'])
class PlaceViewSet(viewsets.ModelViewSet):
    """
    Viewset für die Klasse Place
    Für Änderungen durch den User, ist eine Authentifizierung nötig.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


@extend_schema(tags=['Teacher'])
class TeacherViewSet(viewsets.ModelViewSet):
    """
    Viewset für die Klasse Teacher
    Für Änderungen durch den User, ist eine Authentifizierung nötig.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


@extend_schema(tags=['Student'])
class StudentViewSet(viewsets.ModelViewSet):
    """
    Viewset für die Klasse Student
    Für Änderungen durch den User, ist eine Authentifizierung nötig.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@extend_schema(tags=['Course'])
class CourseViewSet(viewsets.ModelViewSet):
    """
    Viewset für die Klasse Course
    Für Änderungen durch den User, ist eine Authentifizierung nötig.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

@extend_schema(tags=['User'])
class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset für die Klasse User
    Für Änderungen durch den User, ist eine Authentifizierung nötig.
    """
    permission_classes = [IsAuthenticatedOrPostOnly]

    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer