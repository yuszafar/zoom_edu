from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from meeting.models import Profile


class ProfileSerializer(ModelSerializer):

    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password', style={'input_type': 'password', 'placeholder': 'Password'})
    class Meta:
        model = Profile
        fields = ['username', 'password', 'level']

    def create(self, validated_data):
        print(validated_data['user'])
        user = get_user_model().objects.create(username=validated_data['user']['username'])
        user.set_password(validated_data['user']['password'])
        user.save()

        profile = Profile.objects.create(user=user, level=validated_data['level'])

        return profile


