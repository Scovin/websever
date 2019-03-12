from django.db import models
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your models here.
class ImageM(models.Model):
    Image = models.ImageField(upload_to='static/images/%Y/%m/%d', null=False, blank=False,max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "VR"

