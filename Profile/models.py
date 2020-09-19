from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    LEVEL = (
        ("Teacher", "Преподаватель"),
        ("Student", "Студент"),
        ("Training_division", "Учебный отдел")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    otchestvo = models.CharField(max_length=255, null=True)
    level = models.CharField(max_length=255, choices=LEVEL)

    def __str__(self):
        return self.user.username


class StudentGroup(models.Model):
    students = models.ManyToManyField(Profile, limit_choices_to={'level': "Student"})
    group_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name
