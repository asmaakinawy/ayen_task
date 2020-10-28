from rest_framework import serializers


class FileUploadRequestSerializer(serializers.Serializer):
    FILE = serializers.FileField(required=True)

    def validate_FILE(self, value):
        if not value.name.split('.')[1] in ["pdf", "pptx"]:
            raise serializers.ValidationError("files should be power points or pdf only")
        return value