# Generated by Django 5.1.2 on 2024-11-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Students", "0002_alter_student_class_assigned"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="students/default.jpg",
                null=True,
                upload_to="students/profile_pictures",
            ),
        ),
    ]