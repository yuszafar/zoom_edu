from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'Index'
urlpatterns = [
    path('', views.IndexView.as_view(), name='Index'),
]
