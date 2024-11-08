# Generated by Django 5.1.2 on 2024-11-01 23:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Class name must contain only letters and spaces.', regex='^[a-zA-Z\\s]+$')])),
                ('academic_year', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Academic year must be in the format 'YYYY-YYYY'.", regex='^\\d{4}-\\d{4}$')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subjects', models.ManyToManyField(blank=True, related_name='classes', to='Subjects.subject')),
            ],
        ),
    ]
