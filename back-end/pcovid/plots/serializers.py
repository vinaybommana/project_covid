from rest_framework import serializers

from .models import DataObject


class DataObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataObject
        fields = ("id", "metric_name", "timestamp", "data")
