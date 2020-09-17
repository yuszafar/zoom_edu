from django.http import JsonResponse
from rest_framework import generics
from .serializers import LessonInfoCreateSerializer, LessonCreateSerializer, LessonInfoSerializer
from meeting.models import LessonInfo, Lesson, LessonTime


class LessonInfoCreateApiView(generics.CreateAPIView):
    queryset = LessonInfo.objects.all()
    serializer_class = LessonInfoCreateSerializer


class LessonCreateApiView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer


class LessonsCalendarListApiView(generics.ListAPIView):

    def get_queryset(self):
        if self.request.GET.get("day"):
            return Lesson.objects.filter(group=self.kwargs["id"], day=self.request.GET.get("day"))
        return Lesson.objects.filter(group=self.kwargs["id"])

    serializer_class = LessonInfoSerializer
