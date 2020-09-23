from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
# Create your views here.
from Lesson.models import LessonTime, LessonInfo, LessonType
from Profile.models import Profile


class LessonsTimeView(generic.ListView):
    template_name = 'lesson/time.html'
    model = LessonTime
    ordering = "number"


class LessonsTimeUpdateView(LoginRequiredMixin, generic.ListView):
    template_name = 'lesson/update/time.html'
    model = LessonTime
    ordering = "number"


class LessonInfoListView(LoginRequiredMixin, generic.ListView):
    template_name = 'lesson/list.html'
    model = LessonInfo

    def get_queryset(self):
        if self.request.user.profile.level == "Training_division":
            return LessonInfo.objects.all()
        elif self.request.user.profile.level == "Teacher":
            return LessonInfo.objects.filter(teacher_id=self.request.user.profile.id)
        elif self.request.user.profile.level == "Student":
            return LessonInfo.objects.filter(lesson__group__in=self.request.user.profile.studentgroup_set.all())


class LessonInfoCreateVirew(LoginRequiredMixin, generic.TemplateView):
    template_name = 'lesson/create/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teacher_list"] = Profile.objects.filter(level="Teacher")
        context["type_list"] = LessonType.objects.all()
        return context