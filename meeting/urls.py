from django.contrib import admin
from django.urls import path
from .views import IndexView
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'meeting'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
