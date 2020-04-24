
from django.db import models
from django.db.models import Model

class Profile(models.Model):
    firstName = models.CharField(max_length=50, null=True)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phoneNumber = models.IntegerField(blank=True)
    department = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return f"My name is {self.firstName, self.lastName}"