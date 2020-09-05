from django.contrib import admin
from .models import Profile, StudentGroup, TeacherInfo, LessonTime, LessonType, Lesson, LessonInfo
# from .models import UserProfile, Message, File, Chat
#
admin.site.register(Profile)
admin.site.register(StudentGroup)
admin.site.register(TeacherInfo)
admin.site.register(LessonTime)
admin.site.register(LessonType)
admin.site.register(Lesson)
admin.site.register(LessonInfo)
