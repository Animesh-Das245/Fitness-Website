from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import uuid

# Create your models here.
from django.db import models

class Appointment(models.Model):
    name=models.CharField(max_length=90)
    email=models.EmailField(max_length=90)
    phone=models.IntegerField()
    state=models.CharField(max_length=90)
    pin=models.IntegerField()
    describe=models.CharField(max_length=1000,default='Null')

    def __str__(self):

        return self.name

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=17,validators=[phone_regex],unique=True)
    email_verified = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4,editable=False)
