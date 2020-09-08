from django.urls import path
from .lessons_time import views
from .profile.views import CreateProfileApiView
app_name = 'api_v1'
urlpatterns = [
    path('lessons/time/list/', views.TimeListApiView.as_view(), name='lesson_time_list'),
    path('lessons/time/<int:id>', views.TimeUpdateView.as_view(), name='lesson_time'),
    path('profile/create/', CreateProfileApiView.as_view(), name='create_profile'),
]