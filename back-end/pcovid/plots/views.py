from rest_framework import generics

from .models import DataObject
from .serializers import DataObjectSerializer


class ListDataObject(generics.ListAPIView):
    queryset = DataObject.objects.all()
    serializer_class = DataObjectSerializer


class DetailDataObject(generics.RetrieveAPIView):
    queryset = DataObject.objects.all()
    serializer_class = DataObjectSerializer
