from rest_framework import generics
from .serializers import CreateGroupSerializer
from meeting.models import StudentGroup


class CreateGroupApiView(generics.CreateAPIView):
    serializer_class = CreateGroupSerializer