from rest_framework import generics
from rest_framework.response import Response

from .serializers import CreateGroupSerializer
from meeting.models import StudentGroup


class CreateGroupApiView(generics.CreateAPIView):
    serializer_class = CreateGroupSerializer

    def post(self, request, *args, **kwargs):
        if request.user.profile.level != "Training_division":
            return Response({'error': 'you not have permission '}, status=401)
        return super(CreateGroupApiView, self).post(request, *args, **kwargs)
