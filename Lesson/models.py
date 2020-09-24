from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from Profile.models import StudentGroup, Profile


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
    zoom_join_url = models.URLField(null=True, blank=True)
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True)
    lesson_time = models.ForeignKey(LessonTime, on_delete=models.CASCADE)
    zoom_start_url = models.URLField(null=True, blank=True)
    zoom_id = models.CharField(null=True, max_length=255)


    def get_start_datetime(self):
        return str(self.day) + "T" + str(self.lesson_time.start)

    def get_end_datetime(self):
        return str(self.day) + "T" + str(self.lesson_time.end)

    def get_less_name(self):
        return self.lesson_info.name

    def get_join_url(self):
        return self.zoom_join_url

    def get_start_url(self):
        return self.zoom_start_url

    def get_less_time_number(self):
        return self.lesson_time.number

    def get_les_info_id(self):
        return self.lesson_info.id