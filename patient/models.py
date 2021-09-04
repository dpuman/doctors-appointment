from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(
        upload_to='patient-profile', null=True, blank=True)

    def __str__(self):
        return self.name
