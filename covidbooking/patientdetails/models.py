

# Create your models here.
from django.db import models

# Create your models here.
class PatientsDetails(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    dob=models.DateField()
    address=models.CharField(max_length=250)
    district=models.CharField(max_length=250)
    firstdose=models.BooleanField()
    seconddose=models.BooleanField()

    def __str__(self):
        return  self.name