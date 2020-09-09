from rest_framework import generics
from .serializers import LessonInfoCreateSerializer, LessonCreateSerializer
from meeting.models import LessonInfo, Lesson


class LessonInfoCreateApiView(generics.CreateAPIView):
    queryset = LessonInfo.objects.all()
    serializer_class = LessonInfoCreateSerializer


class LessonCreateApiView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer

