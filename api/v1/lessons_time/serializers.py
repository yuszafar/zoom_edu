from rest_framework.serializers import ModelSerializer, HiddenField

from Lesson.models import LessonTime


class LessonsTimeSerializer(ModelSerializer):
    class Meta:
        model = LessonTime
        fields = '__all__'


class LessonsUpdateSerializer(ModelSerializer):
    class Meta:
        model = LessonTime
        fields = ('start', 'end')
