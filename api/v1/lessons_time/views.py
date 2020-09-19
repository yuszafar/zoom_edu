from rest_framework import generics
from rest_framework.response import Response

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

    def put(self, request, *args, **kwargs):
        if request.user.profile.level != "Training_division":
            return Response({'error': 'you not have permission '}, status=401)
        return super(TimeUpdateView, self).put(request, *args, **kwargs)
