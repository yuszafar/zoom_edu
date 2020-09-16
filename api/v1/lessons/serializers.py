from django.db.migrations import serializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from meeting.models import LessonInfo, Lesson, LessonTime


class LessonInfoCreateSerializer(ModelSerializer):
    class Meta:
        model = LessonInfo
        fields = '__all__'

class LessonCreateSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonInfoSerializer(ModelSerializer):
    start = serializers.CharField(source='get_start_datetime')
    end = serializers.CharField(source='get_end_datetime')
    title = serializers.CharField(source='get_less_name')
    url = serializers.CharField(source='get_url')
    class Meta:
        model = Lesson
        fields = ['start', 'end', 'title', 'url']

