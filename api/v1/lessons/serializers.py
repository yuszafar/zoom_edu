from rest_framework.serializers import ModelSerializer
from meeting.models import LessonInfo


class LessonInfoCreateSerializer(ModelSerializer):
    class Meta:
        model = LessonInfo
        fields = '__all__'

