from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'meeting'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('time/', views.LessonsTimeView.as_view(), name='time'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
