from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from Lesson.models import LessonInfo, LessonTime
from Profile.models import StudentGroup


class CalendarRouterView(LoginRequiredMixin, generic.View):
    def get(self, request):
        if request.user.profile.level == "Teacher":
            return HttpResponseRedirect(reverse_lazy('Index:calendar_teacher'))
        elif request.user.profile.level == "Student":
            return HttpResponseRedirect(reverse_lazy('Index:calendar_student'))
        elif request.user.profile.level == "Training_division":
            return HttpResponseRedirect(reverse_lazy('Index:calendar_list'))


class CalendarListView(LoginRequiredMixin, generic.ListView):
    template_name = 'calendar_list.html'
    model = StudentGroup


class CalendarDetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'calendar_detail.html'
    model = StudentGroup

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lesson_info_list"] = LessonInfo.objects.all()
        context["lesson_time_list"] = LessonTime.objects.all()
        return context


class TeacherCalendarView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'teacher_calendar.html'


class StudentCalendarView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'student_calendar.html'
