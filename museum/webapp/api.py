import json
import datetime

from django.shortcuts import get_object_or_404

#cma_seminar
from models import Collection
                 
#REST framework
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response as RestResponse
from rest_framework.authentication import TokenAuthentication


from serializers import (
    ItemSerializer,
)

class ItemView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, id_uuid):
        
        queryset = get_object_or_404(Collection, col_uuid=id_uuid)
        serializer_class = ItemSerializer(queryset)
        
        return RestResponse(serializer_class.data)