from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Profile.models import Profile, StudentGroup


class ProfileSerializer(ModelSerializer):

    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password', style={'input_type': 'password', 'placeholder': 'Password'})
    class Meta:
        model = Profile
        fields = ['username', 'password', 'first_name', 'last_name', 'otchestvo', 'level']

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data['user']['username'])
        user.set_password(validated_data['user']['password'])

        user.save()

        profile = Profile.objects.create(user=user)
        profile.first_name = validated_data['first_name']
        profile.last_name = validated_data['last_name']
        profile.otchestvo = validated_data['otchestvo']
        profile.level = validated_data['level']
        profile.save()
        return profile


class CreateGroupSerializer(ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = '__all__'

