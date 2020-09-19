from rest_framework.serializers import ModelSerializer

from Profile.models import StudentGroup


class CreateGroupSerializer(ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = '__all__'
