from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import LessonTime, LessonInfo, Profile, LessonType, StudentGroup


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base.html'


class CalendarRouterView(generic.View):
    def get(self, request):
        if request.user.profile.level == "Teacher":
            return HttpResponseRedirect(reverse_lazy('meeting:calendar_teacher'))
        elif request.user.profile.level == "Student":
            return HttpResponseRedirect(reverse_lazy('meeting:calendar_student'))
        elif request.user.profile.level == "Training_division":
            return HttpResponseRedirect(reverse_lazy('meeting:calendar_list'))

class CalendarListView(generic.ListView):
    template_name = 'calendar_list.html'
    model = StudentGroup


class CalendarDetailView(generic.DeleteView):
    template_name = 'calendar_detail.html'
    model = StudentGroup
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lesson_info_list"] = LessonInfo.objects.all()
        context["lesson_time_list"] = LessonTime.objects.all()
        return context


class TeacherCalendarView(generic.TemplateView):
    template_name = 'teacher_calendar.html'


class StudentCalendarView(generic.TemplateView):
    template_name = 'student_calendar.html'


class LessonsTimeView(generic.ListView):
    template_name = 'lessons_time.html'
    model = LessonTime
    ordering = "number"



class LessonsTimeUpdateView(generic.ListView):
    template_name = 'lessons_time_update.html'
    model = LessonTime
    ordering = "number"


class CreatUserView(generic.TemplateView):
    template_name = 'create_user.html'


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


class GroupListView(generic.ListView):
    template_name = 'group_list.html'
    model = StudentGroup


class GroupCreateView(generic.TemplateView):
    template_name = 'create_group.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student_list"] = Profile.objects.filter(level="Student")
        return context
