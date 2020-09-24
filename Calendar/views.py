from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from Lesson.models import LessonInfo, LessonTime
from Profile.models import StudentGroup




class CalendarListView(LoginRequiredMixin, generic.ListView):
    template_name = 'calendar/list.html'
    model = StudentGroup
    def get_queryset(self):
        if self.request.user.profile.level == "Training_division":
            return StudentGroup.objects.all()
        elif self.request.user.profile.level == "Teacher":
            return StudentGroup.objects.filter(lesson__lesson_info__teacher=self.request.user.profile).distinct().all()
        elif self.request.user.profile.level == "Student":
            return self.request.user.profile.studentgroup_set.all()
        return StudentGroup.objects.none()


class CalendarUpdateView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'calendar/update/calendar.html'
    model = StudentGroup

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lesson_info_list"] = LessonInfo.objects.all()
        context["lesson_time_list"] = LessonTime.objects.all()
        return context


class CalendarDetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'calendar/detail.html'
    model = StudentGroup

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lesson_info_list"] = LessonInfo.objects.all()
        context["lesson_time_list"] = LessonTime.objects.all()
        return context


