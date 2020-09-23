from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Lesson.models import LessonInfo, Lesson, LessonTime
from .serializers import LessonInfoCreateSerializer, LessonCreateSerializer, LessonInfoSerializer, \
    LessonDeleteSerializer, LessonsTimeSerializer, LessonsUpdateSerializer


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