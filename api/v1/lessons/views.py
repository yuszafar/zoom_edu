from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response

from Lesson.models import LessonInfo, Lesson
from .serializers import LessonInfoCreateSerializer, LessonCreateSerializer, LessonInfoSerializer, LessonDeleteSerializer


class LessonInfoCreateApiView(generics.CreateAPIView):
    queryset = LessonInfo.objects.all()
    serializer_class = LessonInfoCreateSerializer

    def post(self, request, *args, **kwargs):
        if request.user.profile.level != "Training_division":
            return Response({'error': 'you not have permission '}, status=401)
        return super(LessonInfoCreateApiView, self).post(request, *args, **kwargs)


class LessonCreateApiView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer

    def post(self, request, *args, **kwargs):
        if request.user.profile.level != "Training_division":
            return Response({'error': 'you not have permission '}, status=401)
        return super(LessonCreateApiView, self).post(request, *args, **kwargs)


class LessonDeleteApiView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    lookup_url_kwarg = "id"
    serializer_class = LessonDeleteSerializer

    def delete(self, request, *args, **kwargs):
        if request.user.profile.level != "Training_division":
            return Response({'error': 'you not have permission '}, status=401)
        return super().delete(request, *args, **kwargs)


class LessonsCalendarListApiView(generics.ListAPIView):

    def get_queryset(self):
        if self.request.GET.get("day"):
            return Lesson.objects.filter(group=self.kwargs["id"], day=self.request.GET.get("day"))
        return Lesson.objects.filter(group=self.kwargs["id"])

    serializer_class = LessonInfoSerializer


class LessonCalendarStudentListApiView(generics.ListAPIView):
    serializer_class = LessonInfoSerializer

    def get_queryset(self):
        return Lesson.objects.filter(lesson_info__teacher_id=self.kwargs["id"])