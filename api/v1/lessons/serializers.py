from rest_framework.serializers import ModelSerializer
from meeting.models import LessonInfo, Lesson


class LessonInfoCreateSerializer(ModelSerializer):
    class Meta:
        model = LessonInfo
        fields = '__all__'

class LessonCreateSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'