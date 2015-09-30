from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import serializers
from models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image


class ItemSerializer(serializers.ModelSerializer):
    
    col_images_galery = ImageSerializer(many=True)
    class Meta:
        model = Collection
        exclude = ('col_uuid', 'col_qr_code')

  