from rest_framework.serializers import ModelSerializer
from meeting.models import LessonTime


class LessonsTimeSerializer(ModelSerializer):
    class Meta:
        model = LessonTime
        fields = '__all__'
