from django.db import models


# Create your models here.

def nameFile(self, filename):
    return '/'.join(['images', str(self.id), filename])


class Student(models.Model):
    f_name = models.CharField(max_length=50, blank=False)
    l_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(format('foo@gmail.com'), unique=True)
    phone_no = models.IntegerField(blank=False)
    dob = models.DateField(format("%d-%m-%Y"), blank=False)
    password = models.IntegerField(blank=False)
    cnic = models.IntegerField(blank=False)
    role = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to=nameFile, blank=True)
