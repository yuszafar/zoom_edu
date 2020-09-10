from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import LessonTime, LessonInfo, Profile, LessonType


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base.html'


class CalendarView(generic.TemplateView):
    template_name = 'calendar_week.html'


class LessonsTimeView(generic.ListView):
    template_name = 'lessons_time.html'
    model = LessonTime
    ordering = "number"


class LessonsTimeUpdateView(generic.ListView):
    template_name = 'lessons_time_update.html'
    model = LessonTime
    ordering = "number"


class CreatUserView(generic.TemplateView):
    template_name = 'crate_user.html'


class LessonInfoListView(generic.ListView):
    template_name = 'lesson_infos.html'
    model = LessonInfo


class LessonInfoCreateVirew(generic.TemplateView):
    template_name = 'create_lesson_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teacher_list"] = Profile.objects.filter(level="Teacher")
        context["type_list"] = LessonType.objects.all()
        return context


class ProfileListView(generic.ListView):
    model = Profile
    template_name = 'profiles.html'
