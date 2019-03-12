

from .models import ImageM

from rest_framework import serializers

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = ImageM
    fields = ('Image','created')