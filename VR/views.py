
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .yolov3 import GetImage
import os
Base_dir = '/Users/liyicong/websever'
class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)

    if file_serializer.is_valid():
      file_serializer.save()
      path = Base_dir+file_serializer.data["Image"]
      name = GetImage(path)
      data = {'name': name}
      return Response(data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

