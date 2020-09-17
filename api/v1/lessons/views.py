from django.http import JsonResponse
from rest_framework import generics
from .serializers import LessonInfoCreateSerializer, LessonCreateSerializer, LessonInfoSerializer, LessonDeleteSerializer
from meeting.models import LessonInfo, Lesson, LessonTime


class LessonInfoCreateApiView(generics.CreateAPIView):
    queryset = LessonInfo.objects.all()
    serializer_class = LessonInfoCreateSerializer


class LessonCreateApiView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer

class LessonDeleteApiView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    lookup_url_kwarg = "id"
    serializer_class = LessonDeleteSerializer

class LessonsCalendarListApiView(generics.ListAPIView):

    def get_queryset(self):
        if self.request.GET.get("day"):
            return Lesson.objects.filter(group=self.kwargs["id"], day=self.request.GET.get("day"))
        return Lesson.objects.filter(group=self.kwargs["id"])

    serializer_class = LessonInfoSerializer
