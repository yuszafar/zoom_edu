from rest_framework import generics
from .serializers import LessonsTimeSerializer, LessonsUpdateSerializer
from meeting.models import LessonTime


class TimeListApiView(generics.ListAPIView):
    queryset = LessonTime.objects.all()
    serializer_class = LessonsTimeSerializer


class TimeUpdateView(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = LessonTime.objects.all()
    serializer_class = LessonsUpdateSerializer
    lookup_url_kwarg = 'id'