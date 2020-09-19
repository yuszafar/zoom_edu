from django.contrib import admin
from .models import TeacherInfo, LessonTime, LessonType, Lesson, LessonInfo
# from .models import UserProfile, Message, File, Chat
#

admin.site.register(LessonTime)
admin.site.register(LessonType)
admin.site.register(Lesson)
admin.site.register(LessonInfo)
admin.site.register(TeacherInfo)