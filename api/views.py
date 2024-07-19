from rest_framework import viewsets

from api.models import TestTaskModel
from api.serializers import TestTaskSerializer


class TestTaskViewSet(viewsets.ModelViewSet):
    queryset = TestTaskModel.objects.all()
    serializer_class = TestTaskSerializer
