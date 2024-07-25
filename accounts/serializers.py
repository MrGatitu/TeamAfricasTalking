# serializers.py

from rest_framework import serializers

class USSDCallbackSerializer(serializers.Serializer):
    sessionId = serializers.CharField(required=False)
    serviceCode = serializers.CharField(required=False)
    phoneNumber = serializers.CharField(required=False)
    text = serializers.CharField(required=False)
