from rest_framework import viewsets
from .models import WorkerProfile
from .serializers import WorkerProfileSerializer
from rest_framework.permissions import IsAuthenticated

class WorkerProfileViewSet(viewsets.ModelViewSet):
    queryset = WorkerProfile.objects.all()
    serializer_class = WorkerProfileSerializer
    permission_classes = [IsAuthenticated]
