from django.urls import path
from . import views

app_name = 'calendar'
urlpatterns = [

    path('list/', views.CalendarListView.as_view(), name='list'),
    path('update/<int:pk>', views.CalendarUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', views.CalendarDetailView.as_view(), name='detail'),

]
