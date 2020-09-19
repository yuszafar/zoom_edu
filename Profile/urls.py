from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'profile'
urlpatterns = [

    path('create/', views.CreatUserView.as_view(), name='create_user'),
    path('list/', views.ProfileListView.as_view(), name='list'),

    path('group/list/', views.GroupListView.as_view(), name='group_list'),
    path('group/create/', views.GroupCreateView.as_view(), name='group_create'),

]
