from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


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


class TeacherInfo(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    position = models.CharField(max_length=255)


class LessonType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class LessonTime(models.Model):
    number = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], unique=True)
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return "%s %s " % (self.number, "пара")


class LessonInfo(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(LessonType, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'level': "Teacher"})

    def __str__(self):
        return self.name


class Lesson(models.Model):
    day = models.DateField()
    lesson_info = models.ForeignKey(LessonInfo, on_delete=models.CASCADE)
    zum_url = models.URLField(null=True, blank=True)
    group = models.ManyToManyField(StudentGroup)
    lesson_time = models.ForeignKey(LessonTime, on_delete=models.CASCADE)
