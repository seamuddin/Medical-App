from django.db import models
from medical_user.models import CustomUser


# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=30)
    data = models.DateField()
