from django.urls import path
from .profile.views import CreateProfileApiView, CreateGroupApiView
from .lessons.views import LessonInfoCreateApiView, LessonCreateApiView, LessonsCalendarListApiView, \
    LessonDeleteApiView, LessonCalendarStudentListApiView, TimeListApiView, TimeUpdateView
app_name = 'api_v1'
urlpatterns = [
    path('lesson/time/list/', TimeListApiView.as_view(), name='lesson_time_list'),
    path('lesson/time/<int:id>', TimeUpdateView.as_view(), name='lesson_time'),
    path('profile/create/', CreateProfileApiView.as_view(), name='create_profile'),
    path('lesson/info/create/', LessonInfoCreateApiView.as_view(), name='create_lesson_info'),
    path('lesson/create/', LessonCreateApiView.as_view(), name='create_lesson'),
    path('lesson/delete/<int:id>', LessonDeleteApiView.as_view(), name='delete_lesson'),
    path('group/create/', CreateGroupApiView.as_view(), name='create_group'),
    path('lesson/calendar/list/<int:id>', LessonsCalendarListApiView.as_view(), name='lesson_list_calendar'),
    path('lesson/calendar/teacher/list/<int:id>', LessonCalendarStudentListApiView.as_view(), name='lesson_teacher_list_calendar'),
    path('lesson/calendar/student/list/<int:id>', LessonsCalendarListApiView.as_view(), name='lesson_list_calendar'),
]