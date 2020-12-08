from rest_framework import serializers
from api.models import Place, Provider, Teacher, Student, Course
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation



class PlaceSerializer(serializers.ModelSerializer):
    """
    Der Serializer für die Klasse Place wird erstellt.
    """
    class Meta:
        """
        Alle Felder des Models werden verwendet.
        """
        model = Place
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    """
    Der Serializer für der die Klasse Provider wird erstellt.
    """
    place_pk = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all(), source='place_fk', write_only=True, label='Place')

    class Meta:
        model = Provider
        fields = '__all__'
        depth = 1


class TeacherSerializer(serializers.ModelSerializer):
    """
    Der Serializer für die Klasse Teacher wird erstellt.
    """
    class Meta:
        model = Teacher
        fields = '__all__'
        depth = 1


class StudentSerializer(serializers.ModelSerializer):
    """
    Der Serializer für die Klasse Student wird erstellt.
    """
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1


class CourseSerializer(serializers.ModelSerializer):
    """
    Der Serializer für die Klasse Course wird erstellt.
    """
    student_pk = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='course_student',
                                                    write_only=True, many=True, label='Student')
    provider_pk = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), source='provider_fk',
                                                     write_only=True, label='Provider')
    teacher_pk = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), source='teacher_fk',
                                                    write_only=True, label='Teacher')

    class Meta:
        """
        Es wird 2 Ebenen tiefer gegangen.
        """
        model = Course
        fields = '__all__'
        depth = 2


class UserSerializer(serializers.ModelSerializer):
    """
    Der Serializer für die Klasse User wird erstellt.
    Diese Klasse wird von Django bereitgestellt.
    """
    class Meta:
        """
        Die Felder werden angegeben und die Bedingungen
        """
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}, 'id': {'read_only': True},
                        'email': {'required': True},
                        'first_name': {'required': True}, 'last_name': {'required': True}}

    def create(self, validated_data):
        """
        Wenn der User erstellt wird, werden die eingegebenen Daten überprürft.
        :param validated_data: es wird untersucht, ob das Password bereits existiert.
        :return: Bei der erfolgreichen Erstellung wird der User zurückgegeben.
        """
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
        """
        Eine Methode, die für die Updatefunkion zuständig ist.
        :param instance:
        :param validated_data: Daten werden validiert. Die Emailadresse darf nur einmal existieren, ansonsten wird
        eine Fehlermeldung audgegeben.
        :return: Der user wird zurückgegeben
        """
        if User.objects.filter(email=validated_data.get('email')).exists():
            raise serializers.ValidationError('Email already registered.')
        return super(UserSerializer, self).update(instance, validated_data)
