from rest_framework import generics
from .serializers import LessonsTimeSerializer
from meeting.models import LessonTime


class ListApiView(generics.ListAPIView):
    queryset = LessonTime.objects.all()
    serializer_class = LessonsTimeSerializer