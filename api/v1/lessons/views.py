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
        return Lesson.objects.filter(group=self.kwargs["id"])

    serializer_class = LessonInfoSerializer
    #
    # def get(self, request, *args, **kwargs):
    #     return JsonResponse({"title": "Event 1", "start": "2020-09-05T09:00:00", "end": "2020-09-05T18:00:00"})
