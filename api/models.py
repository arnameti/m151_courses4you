from django.db import models


# Create your models here.

# In der Datei models.py werden nun die Klassen erstellt. Das werden dann die Tabellen sein.
# D.h man kann Tablllen erstellen ohne eine Zeile sql-Code zu schreiben.
# Der Ort wird erstellt. Bei postcode ist unique auf Ture, damit nicht der selbe Ort zwei Mal erstellt werden kann.
from django.http import Http404


class Place (models.Model):
    postcode = models.CharField(null=False, max_length=4, unique=True)
    place_name = models.CharField(null=False, max_length=255)

    def __str__(self):
        return '{} {}'.format(self.postcode, self.place_name)



# Der Anbieter wird erstellt. Ein ForeignKey zeigt auf die Tabelle Place. Ein Anbieter kann nur eine Anchrift haben,
# eine Anschrift kann aber 0, 1 oder mehrere verschiedene Anbieter haben.
# mit unique=True bei dem Attribut name wird sichergestellt, dass nicht der selbe Anbeter zweimal erstellt wird.
class Provider (models.Model):
    name = models.CharField(null=False, max_length=512, unique=True)
    place_fk = models.ForeignKey(Place, null=False, on_delete=models.RESTRICT)

    def __str__(self):
        return '{}'.format(self.name)

# Der Lehrende wird erstellt.
# mit unique=True bei dem Attribut email wird sichergestellt, dass eine Email-Adresse nur einmal vorkommt, die
# nur einer bestimmten Person (Teacher oder Student) gehört.
class Teacher (models.Model):
    first_name = models.CharField(null=False, max_length=255)
    last_name = models.CharField(null=False, max_length=255)
    email = models.CharField(null=False, max_length=512, unique=True)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.email)

# Der Lernende wird erstellt.
# mit unique=True bei dem Attribut email wird sichergestellt, dass eine Email-Adresse nur einmal vorkommt, die nur
# einer bestimmten Person (Teacher oder Student) gehört.
class Student (models.Model):
    first_name = models.CharField(null=False, max_length=255)
    last_name = models.CharField(null=False, max_length=255)
    email = models.CharField(null=False, max_length=512, unique=True)


    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name, self.email)

# Hier wird die Tabelle für die Kurse erstellt, die angeboten werden.
# mit unique=True bei dem Attribut email wird sichergestellt, dass es einen bestimmten Kurs nur einmal gibt,
# da Courses4You einen bestimmten Kurs nur an einem bestimmten Ort anbietet.
class Course (models.Model):
    name = models.CharField(null=False, max_length=1024, unique=True)

    provider_fk = models.ForeignKey(Provider, null=False, on_delete=models.CASCADE)
    teacher_fk = models.ForeignKey(Teacher, null=False, on_delete=models.RESTRICT)
    course_student = models.ManyToManyField(Student, related_name='course_student')

    def __str__(self):
        return '{}'.format(self.name, self.date)
