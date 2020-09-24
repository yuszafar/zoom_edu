import datetime

from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

from Lesson.models import Lesson


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'index.html'
    model = Lesson

    def get_queryset(self):
        now = datetime.datetime.now()
        if self.request.user.profile.level == "Training_division":
            return Lesson.objects.filter(Q(day=now.date(), lesson_time__start__gte=now.time())
                                         | Q(day__gt=now.date())).order_by('day', 'lesson_time__start')
        elif self.request.user.profile.level == "Teacher":
            return Lesson.objects.filter(Q(day=now.date(), lesson_time__start__gte=now.time())
                                         | Q(day__gt=now.date()),
                                         lesson_info__teacher=self.request.user.profile
                                         ).order_by('day', 'lesson_time__start')

        elif self.request.user.profile.level == "Student":
            return Lesson.objects.filter(Q(day=now.date(), lesson_time__start__gte=now.time())
                                         | Q(day__gt=now.date()),
                                         group__in=self.request.user.profile.studentgroup_set.all()).order_by('day', 'lesson_time__start')
