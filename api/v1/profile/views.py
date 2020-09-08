from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from meeting.models import Profile
from .serializers import ProfileSerializer


class CreateProfileApiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer