from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from Profile.models import StudentGroup, Profile


class GroupListView(LoginRequiredMixin, generic.ListView):
    template_name = 'profile/group/list.html'
    model = StudentGroup


class GroupCreateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile/create/group.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student_list"] = Profile.objects.filter(level="Student")
        return context


class CreatUserView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile/create/profile.html'


class ProfileListView(LoginRequiredMixin, generic.ListView):
    model = Profile
    template_name = 'profile/list.html'


class GroupDetailView(LoginRequiredMixin, generic.DetailView):
    model = StudentGroup
    template_name = 'profile/group/detail.html'
