from django.core.validators import RegexValidator, EmailValidator
from django.db import models

from Class.models import Class


class Student(models.Model):
    # Personal Information
    name_validator = RegexValidator(
        regex=r"^[a-zA-Z]+$", message="Name must contain only letters."
    )
    profile_picture = models.ImageField(
        upload_to="students/profile_pictures", blank=True, null=True
    )
    first_name = models.CharField(max_length=100, validators=[name_validator])
    last_name = models.CharField(max_length=100, validators=[name_validator])
    other_names = models.CharField(
        max_length=100, blank=True, null=True, validators=[name_validator]
    )
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[("Male", "Male"), ("Female", "Female")],
        blank=True,
        null=True,
    )

    # Parent Information
    parent_first_name = models.CharField(max_length=100, validators=[name_validator])
    parent_last_name = models.CharField(max_length=100, validators=[name_validator])
    parent_other_names = models.CharField(
        max_length=100, blank=True, null=True, validators=[name_validator]
    )
    parent_email = models.EmailField(validators=[EmailValidator()])
    phone_validator = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    parent_phone_number_1 = models.CharField(
        max_length=15, validators=[phone_validator]
    )
    parent_phone_number_2 = models.CharField(
        max_length=15, blank=True, null=True, validators=[phone_validator]
    )
    parent_occupation = models.CharField(max_length=100, validators=[name_validator])

    # Address Information
    address = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, validators=[name_validator])

    # School Information
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
