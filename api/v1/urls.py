from django.urls import path
from .lessons_time import views
from .profile.views import CreateProfileApiView
from .lessons.views import LessonInfoCreateApiView, LessonCreateApiView
from .student_group.views import CreateGroupApiView
app_name = 'api_v1'
urlpatterns = [
    path('lessons/time/list/', views.TimeListApiView.as_view(), name='lesson_time_list'),
    path('lessons/time/<int:id>', views.TimeUpdateView.as_view(), name='lesson_time'),
    path('profile/create/', CreateProfileApiView.as_view(), name='create_profile'),
    path('lessons/info/create/', LessonInfoCreateApiView.as_view(), name='create_lesson_info'),
    path('lessons/create/', LessonCreateApiView.as_view(), name='create_lesson'),
    path('group/create/', CreateGroupApiView.as_view(), name='create_group'),
]