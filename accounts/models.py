from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from .choices import (
    gender_choice,
    user_choice,
    nationality_choice,
    religion_choice,
    user_bloodgroup_choice,
    education_choice,
    course_type_choices,
    address_type,
)
from phone_field import PhoneField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=45, null=True)
    Age = models.PositiveIntegerField(null=True)
    phone_number = PhoneField(null=True, help_text="Enter Your Contact Number")
    user_type = models.CharField(max_length=16, choices=user_choice, null=True)

    def __str__(self):
        return str(self.name)


class personal_information(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    bloodgroup = models.CharField(
        choices=user_bloodgroup_choice, max_length=12, null=True
    )
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=gender_choice, null=True)
    father_name = models.CharField(max_length=128, null=True)
    father_occupation = models.CharField(max_length=128, null=True)
    mother_name = models.CharField(max_length=128, null=True)
    mother_occupation = models.CharField(max_length=128, null=True)
    religion = models.CharField(max_length=20, null=True, choices=religion_choice)
    nationality = models.CharField(max_length=20, null=True, choices=nationality_choice)

    def __str__(self):
        return str(self.user)


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Address_Type = models.CharField(choices=address_type, null=True, max_length=64)
    Door_Number = models.CharField(max_length=150)
    Street = models.CharField(max_length=150)
    Address_Line_1 = models.CharField(max_length=150)
    Address_line_2 = models.CharField(max_length=150)
    Land_Mark = models.CharField(max_length=150)
    Pincode = models.CharField(max_length=150)

    def __str__(self):
        return self.user


class educational_information(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    education = models.CharField(null=True, max_length=64, choices=education_choice)
    course = models.CharField(null=True, max_length=64)
    specialization = models.CharField(null=True, max_length=64)
    university_or_institute = models.CharField(null=True, max_length=64)
    course_type = models.CharField(
        null=True, max_length=64, choices=course_type_choices
    )
    Date_of_passing_out = models.DateField(null=True)
    percentage_or_grade_accquired = models.CharField(null=True, max_length=64)

    def __str__(self):
        return self.user

