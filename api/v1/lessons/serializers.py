from django.db.migrations import serializer
import requests
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Lesson.models import LessonInfo, Lesson, LessonTime


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
        obj = Lesson.objects.filter(group=validated_data.get("group"), day=validated_data.get("day"),
                                    lesson_time=validated_data.get("lesson_time"))
        if obj:

            lesson = obj[0]
            lesson.lesson_info = validated_data.get("lesson_info")
            lesson.save()
            return lesson
        else:
            answer = Lesson.objects.create(**validated_data)
            headers = {
                "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IkFfWWU0Qm9uUnRxcy00cDVDd1d6SnciLCJleHAiOjE2MDE0NjQ0NjEsImlhdCI6MTYwMDg1OTY2MX0.R6fAQA3f5IzE2KlIjwHgHHZQj55q9bJJzus2mizp1RQ",
                "content-type": "application/json"
            }
            data = {
                "topic": answer.get_less_name(),
                "type": 2,
                "start_time": answer.get_start_datetime(),
                "duration": 90,
                "timezone": "Asia/Tashkent"
            }
            # print(data)
            response = requests.post(url='https://api.zoom.us/v2/users/XhbF5D0XTuSkNXprvMZRZQ/meetings', json=data, headers=headers)
            # print(response.status_code)
            answer.zum_url = response.json()['join_url']
            #
            answer.save()
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
        fields = ['id', 'start', 'end', 'title', 'url', 'less_numb', 'less_info_id']


class LessonsTimeSerializer(ModelSerializer):
    class Meta:
        model = LessonTime
        fields = '__all__'


class LessonsUpdateSerializer(ModelSerializer):
    class Meta:
        model = LessonTime
        fields = ('start', 'end')
