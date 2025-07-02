from rest_framework import serializers
from .models import Job, Application
from users.serializers import UserSerializer

class JobSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'client', 'title', 'description', 'category', 'budget', 'location', 'posted_at', 'is_open']

    def create(self, validated_data):
        validated_data['client'] = self.context['request'].user
        return super().create(validated_data)

class ApplicationSerializer(serializers.ModelSerializer):
    worker = UserSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'job', 'worker', 'message', 'status', 'applied_at']

    def create(self, validated_data):
        validated_data['worker'] = self.context['request'].user
        return super().create(validated_data)
