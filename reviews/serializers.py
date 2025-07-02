from rest_framework import serializers
from .models import Review
from users.serializers import UserSerializer
from jobs.models import Job

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = UserSerializer(read_only=True)
    reviewed = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'job', 'reviewer', 'reviewed', 'rating', 'comment', 'created_at']

    def create(self, validated_data):
        validated_data['reviewer'] = self.context['request'].user
        return super().create(validated_data)
