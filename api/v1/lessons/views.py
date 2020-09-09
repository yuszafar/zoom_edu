from rest_framework import generics
from .serializers import LessonInfoCreateSerializer
from meeting.models import LessonInfo


class LessonInfoCreateApiView(generics.CreateAPIView):
    queryset = LessonInfo.objects.all()
    serializer_class = LessonInfoCreateSerializer

