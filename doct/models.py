
from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.


class Days(models.Model):
    day_names = (
        ('saturday', 'Saturday '),
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
    )
    day = models.CharField(choices=day_names, max_length=20)

    def __str__(self):
        return self.day


class Doctor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='doct-profile', null=True, blank=True)
    appointment_days = models.ManyToManyField(Days)
    visiting_charge = models.FloatField(null=False, blank=False)
    title = models.CharField(max_length=100, null=True, blank=True)
    degree = models.CharField(max_length=100, null=False, blank=False)
    institution = models.CharField(max_length=200, null=True, blank=True)
    year_of_degree = models.DateField(null=True, blank=True)
    max_patient = models.IntegerField(null=True, blank=True)
    appointment_took = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    appointment_status = (
        ('present', 'Present'),
        ('absent', 'Absent')
    )

    doctor = models.OneToOneField(
        Doctor, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.OneToOneField(
        Patient, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    problem = models.TextField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, choices=appointment_status)


class Prescription(models.Model):
    Doctor = models.OneToOneField(
        Doctor, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.OneToOneField(
        Patient, on_delete=models.CASCADE, null=True, blank=True)
    prescription = models.TextField(blank=True, null=True)
