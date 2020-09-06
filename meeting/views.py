from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import LessonTime


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base.html'


class CalendarView(generic.TemplateView):
    template_name = 'calendar_week.html'


class LessonsTimeView(generic.ListView):
    template_name = 'lessons_time.html'
    model = LessonTime
    ordering = "number"


