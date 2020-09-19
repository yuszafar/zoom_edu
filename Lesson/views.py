from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
# Create your views here.
from Lesson.models import LessonTime, LessonInfo, LessonType
from Profile.models import Profile


class LessonsTimeView(generic.ListView):
    template_name = 'lessons_time.html'
    model = LessonTime
    ordering = "number"


class LessonsTimeUpdateView(LoginRequiredMixin, generic.ListView):
    template_name = 'lessons_time_update.html'
    model = LessonTime
    ordering = "number"


class CreatUserView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'create_user.html'


class LessonInfoListView(LoginRequiredMixin, generic.ListView):
    template_name = 'lesson_infos.html'
    model = LessonInfo


class LessonInfoCreateVirew(LoginRequiredMixin, generic.TemplateView):
    template_name = 'create_lesson_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teacher_list"] = Profile.objects.filter(level="Teacher")
        context["type_list"] = LessonType.objects.all()
        return context