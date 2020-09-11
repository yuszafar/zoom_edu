from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'meeting'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),

    path('user/create/', views.CreatUserView.as_view(), name='create_user'),
    path('user/list/', views.ProfileListView.as_view(), name='user_list'),

    path('group/list/', views.GroupListView.as_view(), name='group_list'),
    path('group/create/', views.GroupCreateView.as_view(), name='group_create'),

    path('time/list/', views.LessonsTimeView.as_view(), name='time'),
    path('time/update/', views.LessonsTimeUpdateView.as_view(), name='time_update'),
    path('lesson_info/list/', views.LessonInfoListView.as_view(), name='lesson_info'),
    path('lesson_info/create/', views.LessonInfoCreateVirew.as_view(), name='lesson_info_create'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
