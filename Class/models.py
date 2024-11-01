from django.core.validators import RegexValidator
from django.db import models

from Subjects.models import Subject


# This is the model for the Class
class Class(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z\s]+$",
                message="Class name must contain only letters and spaces.",
            )
        ],
    )
    academic_year = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\d{4}-\d{4}$",
                message="Academic year must be in the format 'YYYY-YYYY'.",
            )
        ],
    )
    subjects = models.ManyToManyField(Subject, related_name="classes", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.academic_year}"
