from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length = 200)
    specialty = models.CharField(max_length = 200)
    def get_absolute_url(self):
        return reverse("index",kwargs={'pk':self.pk})


class  Patient(models.Model):
    name = models.CharField(max_length = 200)
    DICOM_FILE = models.FileField(upload_to='DICOM/', default="")
    Image   = models.ImageField(upload_to='3D/', null=True, blank=True)
    Result = models.IntegerField(null = True)
