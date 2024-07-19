from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from api.models import TestTaskModel


class TestTaskSerializer(serializers.ModelSerializer):
    picture = Base64ImageField()

    class Meta:
        model = TestTaskModel
        fields = ("text", "picture")
