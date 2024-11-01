# Generated by Django 5.1.2 on 2024-11-01 23:24

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Class', '0001_initial'),
        ('Students', '0001_initial'),
        ('Subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(message='Grade type name must contain only letters and spaces.', regex='^[a-zA-Z\\s]+$')])),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('term', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Term must contain only letters, numbers, and spaces.', regex='^[a-zA-Z0-9\\s]+$')])),
                ('class_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Class.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subjects.subject')),
                ('grade_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grades.gradetype')),
            ],
        ),
    ]