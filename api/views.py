from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import AnbieterSerializer, AnschriftSerializer, KursleiterSerializer, KursteilnehmerSerializer, KursSerializer
from .models import Anbieter, Anschrift, Kursleiter, Kursteilnehmer, Kurs

# Create your views here.
class AnbieterViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Anbieter.objects.all()
    serializer_class = AnbieterSerializer


class AnschriftViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Anschrift.objects.all()
    serializer_class = AnschriftSerializer


class KursleiterViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Kursleiter.objects.all()
    serializer_class = KursleiterSerializer


class KursteilnehmerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Kursteilnehmer.objects.all()
    serializer_class = KursteilnehmerSerializer


class KursViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
