# serializers.py

from rest_framework import serializers
from .models import Barang


class BarangSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Barang
        fields = ('nama_barang', 'harga_barang', 'stock_barang')