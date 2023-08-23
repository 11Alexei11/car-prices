from django.db import models

# Create your models here.
class User(models.Model):
    ID = models.BigAutoField(primary_key=True, auto_created=True)
    NAME = models.CharField(max_length=30)
    EMAIL = models.CharField(max_length=30)
    REGISTRATION_DATE = models.DateTimeField(auto_now_add=True)
    PASSWORD = models.CharField(max_length=255)
    last_login = models.DateTimeField()