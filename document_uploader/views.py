from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .request_serializers import FileUploadRequestSerializer
from .response_serializers import FileUploadResponseSERIALIZER, FileUploadResponseOBJECT
from .models import Uploads

class UploadFile(APIView):
    def post(self, request, format=None):
        serializer = FileUploadRequestSerializer(data=request.data)
        if not serializer.is_valid():
            response = FileUploadResponseOBJECT(TXNSTATUS="502")
            response = FileUploadResponseSERIALIZER(response)
            return Response(response.data)
        file = serializer.validated_data["FILE"]
        Uploads.objects.create_new_file(file)
        files = Uploads.objects.get_files()
        response = FileUploadResponseOBJECT(TXNSTATUS=200, FILES=files)
        response = FileUploadResponseSERIALIZER(response)
        return Response(response.data)

    def get(self, request, format=None):
        keywords = request.GET.get("keywords", None)
        files = Uploads.objects.get_files(keywords=keywords)
        response = FileUploadResponseOBJECT(TXNSTATUS=200, FILES=files)
        response = FileUploadResponseSERIALIZER(response)
        return Response(response.data)