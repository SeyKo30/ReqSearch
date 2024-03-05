from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    EDR = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=255, default='')
    responsible_person = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class UploadedDocument(models.Model):
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(null=True, blank=True)

