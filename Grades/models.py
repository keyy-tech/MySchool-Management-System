from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models

from Class.models import Class
from Students.models import Student
from Subjects.models import Subject


class GradeType(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z\s]+$",
                message="Grade type name must contain only letters and spaces.",
            )
        ],
    )

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade_type = models.ForeignKey(GradeType, on_delete=models.CASCADE)
    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(100.00)],
    )
    term = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9\s]+$",
                message="Term must contain only letters, numbers, and spaces.",
            )
        ],
    )

    def __str__(self):
        return f"{self.student} - {self.subject} ({self.grade_type}) - {self.score}"
