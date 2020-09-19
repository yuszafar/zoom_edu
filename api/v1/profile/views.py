from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Profile.models import Profile
from .serializers import ProfileSerializer


class CreateProfileApiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        if request.user.profile.level != "Training_division":
            return Response({'error': 'you not have permission '}, status=401)
        return super(CreateProfileApiView, self).post(request, *args, **kwargs)