# Generated by Django 5.1.2 on 2024-11-07 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Students", "0003_alter_student_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="media/default.jpg",
                null=True,
                upload_to="students/profile_pictures",
            ),
        ),
    ]
