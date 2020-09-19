from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'lesson'
urlpatterns = [

    path('time/list/', views.LessonsTimeView.as_view(), name='time'),
    path('time/update/', views.LessonsTimeUpdateView.as_view(), name='time_update'),
    path('info/list/', views.LessonInfoListView.as_view(), name='info'),
    path('info/create/', views.LessonInfoCreateVirew.as_view(), name='lesson_info_create'),


]
