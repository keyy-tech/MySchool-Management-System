# Generated by Django 5.1.2 on 2024-11-01 23:24

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Class", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="students/profile_pictures"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Name must contain only letters.",
                                regex="^[a-zA-Z]+$",
                            )
                        ],
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Name must contain only letters.",
                                regex="^[a-zA-Z]+$",
                            )
                        ],
                    ),
                ),
                (
                    "other_names",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Name must contain only letters.",
                                regex="^[a-zA-Z]+$",
                            )
                        ],
                    ),
                ),
                ("date_of_birth", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("Male", "Male"), ("Female", "Female")],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "parent_first_name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Name must contain only letters.",
                                regex="^[a-zA-Z]+$",
                            )
                        ],
                    ),
                ),
                (
                    "parent_last_name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Name must contain only letters.",
                                regex="^[a-zA-Z]+$",
                            )
                        ],
                    ),
                ),
                (
                    "parent_other_names",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Name must contain only letters.",
                                regex="^[a-zA-Z]+$",
                            )
                        ],
                    ),
                ),
                (
                    "parent_email",
                    models.EmailField(
                        max_length=254,
                        validators=[django.core.validators.EmailValidator()],
                    ),
                ),
                (
                    "parent_phone_number_1",
                    models.CharField(
                        max_length=15,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                (
                    "parent_phone_number_2",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                (
                    "parent_occupation",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Name must contain only letters.",
                                regex="^[a-zA-Z]+$",
                            )
                        ],
                    ),
                ),
                ("address", models.CharField(max_length=255)),
                ("address_1", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "city",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Name must contain only letters.",
                                regex="^[a-zA-Z]+$",
                            )
                        ],
                    ),
                ),
                ("date_enrolled", models.DateField()),
                (
                    "class_assigned",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Class.class"
                    ),
                ),
            ],
        ),
    ]
