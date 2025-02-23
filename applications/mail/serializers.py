from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    email_list = serializers.ListField(
        child=serializers.EmailField(required=True),
        required=True,
    )
    subject = serializers.CharField(max_length=150, required=True)
    body = serializers.CharField(max_length=500, required=True)
