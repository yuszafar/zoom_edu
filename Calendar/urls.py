from django.urls import path
from . import views

app_name = 'calendar'
urlpatterns = [

    path('calendar/', views.CalendarRouterView.as_view(), name='calendar_index'),
    path('list/', views.CalendarListView.as_view(), name='calendar_list'),
    path('detail/<int:pk>', views.CalendarDetailView.as_view(), name='calendar_detail'),
    path('teacher/', views.TeacherCalendarView.as_view(), name='calendar_teacher'),

    path('student/', views.StudentCalendarView.as_view(), name='calendar_student'),


]
