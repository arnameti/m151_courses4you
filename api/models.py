from django.db import models

# Create your models here.


class Anschrift (models.Model):
    plz = models.CharField(null=False, max_length=4)
    ortsname = models.CharField(null=False, max_length=512)

    def __str__(self):
        return '{} {}'.format(self.plz, self.ortsname)

class Anbieter (models.Model):
    name = models.CharField(null=False, max_length=512)
    anschrift_fk = models.OneToOneField(Anschrift, null=False, on_delete=models.RESTRICT, primary_key=True)

    def __str__(self):
        return '{}'.format(self.name)


class Kursleiter (models.Model):
    first_name = models.CharField(null=False, max_length=255)
    last_name = models.CharField(null=False, max_length=255)
    email = models.CharField(null=False, max_length=512)
    anschrift_fk = models.OneToOneField(Anschrift,null=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.email)


class Kursteilnehmer (models.Model):
    first_name = models.CharField(null=False, max_length=255)
    last_name = models.CharField(null=False, max_length=255)
    email = models.CharField(null=False, max_length=512)


    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name, self.email)


class Kurs (models.Model):
    beschreibung = models.CharField(null=False, max_length=1024)
    date = models.DateField

    anbieter_fk = models.ForeignKey(Anbieter, null=False, on_delete=models.CASCADE)
    kursleiter_fk = models.ForeignKey(Kursleiter, null=False, on_delete=models.CASCADE)
    kurs_kursteilnehmer = models.ManyToManyField(Kursteilnehmer, related_name='kurs_kursteilnehmer')

    def __str__(self):
        return '{}'.format(self.beschreibung, self.date)

