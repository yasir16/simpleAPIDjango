from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets

from .serializers import BarangSerializer
from .models import Barang

class BarangViewSet(viewsets.ModelViewSet):
    queryset = Barang.objects.all().order_by('id')
    serializer_class = BarangSerializer