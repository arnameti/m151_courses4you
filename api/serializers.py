from rest_framework import serializers
from api.models import Anschrift, Anbieter, Kursleiter, Kursteilnehmer, Kurs

class AnschriftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anschrift
        fields = ['plz','ortsname']

class AnbieterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anbieter
        fields =('name')
        depth = 1

class KursleiterSerializer(serializers.ModelSerializer):
    class Meta:
        model: Kursleiter
        fields = ['first_name', 'last_name', 'email']
        depth = 1

class KursteilnehmerSerializer(serializers.ModelSerializer):
    class Meta:
        model: Kursteilnehmer
        fields = ['first_name', 'last_name', 'email']
        depth = 1

class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model: Kurs
        fields = ['beschreibung', 'date']
        depth = 1


