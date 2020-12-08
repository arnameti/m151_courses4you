from django.db import models


# Create your models here.
class Place (models.Model):
    """
    Die Klasse Place mit den dazugehörigen Feldern wird erstellt.
    """
    postcode = models.CharField(null=False, max_length=4, unique=True)
    place_name = models.CharField(null=False, max_length=255)

    def __str__(self):
        return '{} {}'.format(self.postcode, self.place_name)

class Provider (models.Model):
    """
    Die Klasse Provider mit den dazugehörigen Feldern wird erstellt.
    Es besteht eine Verbindung zu der Klasse Place
    """
    name = models.CharField(null=False, max_length=512, unique=True)
    place_fk = models.ForeignKey(Place, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

class Teacher (models.Model):
    """
    Die Klasse Teacher mit den dazugehörigen Feldern wird erstellt.
    """
    first_name = models.CharField(null=False, max_length=255)
    last_name = models.CharField(null=False, max_length=255)
    email = models.CharField(null=False, max_length=512, unique=True)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.email)

class Student (models.Model):
    """
    Die Klasse Student mit den dazuehörigen Feldern wird erstellt.
    """
    first_name = models.CharField(null=False, max_length=255)
    last_name = models.CharField(null=False, max_length=255)
    email = models.CharField(null=False, max_length=512, unique=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name, self.email)

class Course (models.Model):
    """
    Die Klasse mit den dazugehörigen Feldern wird erstellt.
    Es besteht eine Verbindung zu den Klassen Provider und Teacher
    so wie eine many-to-many Verbindung zu der Klasse Student.
    """
    name = models.CharField(null=False, max_length=1024, unique=True)
    provider_fk = models.ForeignKey(Provider, null=False, on_delete=models.CASCADE)
    teacher_fk = models.ForeignKey(Teacher, null=False, on_delete=models.RESTRICT)
    course_student = models.ManyToManyField(Student, related_name='course_student')

    def __str__(self):
        return '{}'.format(self.name, self.date)
