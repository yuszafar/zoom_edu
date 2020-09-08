from rest_framework import generics
from .serializers import LessonsTimeSerializer, LessonsUpdateSerializer
from meeting.models import LessonTime
from rest_framework.permissions import IsAuthenticated


class TimeListApiView(generics.ListAPIView):
    queryset = LessonTime.objects.all()
    serializer_class = LessonsTimeSerializer


class TimeUpdateView(generics.UpdateAPIView, generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = LessonTime.objects.all()
    serializer_class = LessonsUpdateSerializer
    lookup_url_kwarg = 'id'

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return super(TimeUpdateView, self).get_permissions()