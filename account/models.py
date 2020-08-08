from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from .choices import gender_choice, user_choice


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=45, null=True)
    gender = models.CharField(max_length=10, choices=gender_choice, null=True)
    Age = models.PositiveIntegerField(null=True)
    user_type = models.CharField(max_length=16, choices=user_choice, null=True)

    def __str__(self):
        return self.name
