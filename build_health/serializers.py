from rest_framework import serializers
from .models import HealthRequests
import datetime


class HealthRequestSerializer(serializers.Serializer):

    class Meta:
        model = HealthRequests

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class DailyReportViewSerializer(serializers.Serializer):

    start = serializers.DateField(required=False, default=datetime.datetime.today().date().strftime("%Y-%m-%d"))
    end = serializers.DateField(required=False, default=datetime.datetime.today().date().strftime("%Y-%m-%d"))

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ImportBuildViewSerializer(serializers.Serializer):

    date = serializers.DateField(required=False, default=datetime.datetime.today().date().strftime("%Y-%m-%d"))

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class HealthRequestViewSerializer(serializers.Serializer):

    type = serializers.ChoiceField(required=True,
                                   allow_blank=False, allow_null=False,
                                   choices=["daily", "hourly"])
    start = serializers.DateTimeField(required=False)
    end = serializers.DateTimeField(required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
