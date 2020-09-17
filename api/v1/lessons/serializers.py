from django.db.migrations import serializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from meeting.models import LessonInfo, Lesson, LessonTime
from ..student_group.serializers import CreateGroupSerializer


class LessonInfoCreateSerializer(ModelSerializer):
    class Meta:
        model = LessonInfo
        fields = '__all__'


class LessonDeleteSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonCreateSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

    def create(self, validated_data):
        print("asd")
        obj = Lesson.objects.filter(group=validated_data.get("group"), day=validated_data.get("day"),
                                    lesson_time=validated_data.get("lesson_time"))
        if obj:

            lesson = obj[0]
            if validated_data.get("lesson_info") != "":
                lesson.lesson_info = validated_data.get("lesson_info")
                lesson.save()
                return lesson
            else:
                print("asdasdasd")
                lesson.delete()
        else:
            answer = Lesson.objects.create(**validated_data)
            return answer


class LessonInfoSerializer(ModelSerializer):
    start = serializers.CharField(source='get_start_datetime')
    end = serializers.CharField(source='get_end_datetime')
    title = serializers.CharField(source='get_less_name')
    url = serializers.CharField(source='get_url')
    less_numb = serializers.CharField(source='get_less_time_number')
    less_info_id = serializers.CharField(source='get_les_info_id')

    class Meta:
        model = Lesson
        fields = ['start', 'end', 'title', 'url', 'less_numb', 'less_info_id']
