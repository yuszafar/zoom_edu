from django.urls import path
from .lessons_time import views
app_name = 'api_v1'
urlpatterns = [
    path('lessons/time/list/', views.ListApiView.as_view(), name='lesson_time_list')
]