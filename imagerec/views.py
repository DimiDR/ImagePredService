from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
from .ml import ImageRecognition
from .models import File

imageRec = ImageRecognition()

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    global imageRec
    
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            
            # get ML prediction and build Responce
            values = imageRec.classifyImage(file_serializer.data["file"])
            values["id"] = file_serializer.data["id"]
            values["file"] = file_serializer.data["file"]

            # delete previously uploaded file
            if file_serializer.data["id"] > 0:
                file = File.objects.get(pk=file_serializer.data["id"] - 1 )
                file.delete()

            return Response(values, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)