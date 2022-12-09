from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Student(models.Model):

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    scholar = models.BooleanField(default=False)
    phone_number = PhoneNumberField(blank=True, null=True)
