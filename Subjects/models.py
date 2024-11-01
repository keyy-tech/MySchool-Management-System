from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z\s]+$",
                message="Subject name must contain only letters and spaces.",
            )
        ],
    )
    code = models.CharField(
        max_length=3,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[A-Z]{3}$",
                message="Subject code must be exactly 3 uppercase letters.",
            )
        ],
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
