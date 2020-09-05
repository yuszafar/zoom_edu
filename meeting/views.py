from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, generic.TemplateView):
    # login_url = 'login/'
    template_name = 'base.html'