from rest_framework import serializers
from rest_csv.models import File


# remember to import the File model
class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class SaveFileSerializer(serializers.Serializer):
    class Meta:
        model = File
        fields = "__all__"


class CsvOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
