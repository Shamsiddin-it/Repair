from rest_framework import serializers
from .models import User, WorkerProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_client', 'is_worker']
        ref_name = 'CustomUserSerializer'
class WorkerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = WorkerProfile
        fields = ['id', 'user', 'skills', 'experience_years', 'hourly_rate', 'location', 'is_available']
