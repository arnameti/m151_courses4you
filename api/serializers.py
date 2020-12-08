from django.http import Http404
from rest_framework import serializers
from api.models import Place, Provider, Teacher, Student, Course
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation


# Hier werden alle Serializers erstellt. Dazu müssen die Models (also die Klassen), die in der Datei models.py erstellt wurden, importiert werden.
# D.h hier werden die Klassen erstellt, die die Serialisierung und Desirialisierung vornehmen.
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


# Mit depth = 1 wird eine Ebene tiefer gegangen. D.h in diesem Fall ist beim Aufruf des Prividers, auch die Anschrift ersichtlich.
class ProviderSerializer(serializers.ModelSerializer):
    place_pk = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all(), source='place_fk', write_only=True,
                                                  label='Place')

    class Meta:
        model = Provider
        fields = '__all__'
        depth = 1


# Der Serializer für die Klasse Teacher.
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        depth = 1


# Der Serializer für die Klasse Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1


# Der Serializer für die Klasse Course
class CourseSerializer(serializers.ModelSerializer):
    student_pk = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='course_student',
                                                    write_only=True, many=True, label='Student')
    provider_pk = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), source='provider_fk',
                                                     write_only=True, label='Provider')
    teacher_pk = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), source='teacher_fk',
                                                    write_only=True, label='Teacher')

    class Meta:
        model = Course
        fields = '__all__'
        depth = 2


# Für diesen Serializer ist kein model erstellt worden. Hier wird von Django der User bereitgestellt, der importiert werden muss.
# Der User muss sich authentifizieren, um die Kurse, Kursteilnehmer etc. erstellen zu können.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}, 'id': {'read_only': True},
                        'email': {'required': True},
                        'first_name': {'required': True}, 'last_name': {'required': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        try:
            if User.objects.filter(email=validated_data.get('email')).exists():
                raise serializers.ValidationError('Email already registered.')
            password_validation.validate_password(password)
        except ValidationError as ve:
            raise serializers.ValidationError({'Password-Errors': [i for i in ve.messages]})
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        if User.objects.filter(email=validated_data.get('email')).exists():
            raise serializers.ValidationError('Email already registered.')
        return super(UserSerializer, self).update(instance, validated_data)
