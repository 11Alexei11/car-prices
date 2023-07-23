from django.db import models

# Create your models here.
class User(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAME = models.CharField(max_length=30)
    SURNAME = models.CharField(max_length=30)
    EMAIL = models.CharField(max_length=30)
    REGISTRATION_DATE = models.DateTimeField()