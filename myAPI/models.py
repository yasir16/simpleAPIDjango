from django.db import models

# Create your models here.


class Barang(models.Model):
    name_barang = models.CharField(max_length=100)
    harga_barang = models.FloatField()
    stock_barang = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name_barang

    
class Penjualan(models.Model):
    total_pembelian = models.FloatField()
    tanggal_penjualan = models.DateTimeField(auto_now_add=True)
    keterangan_penjualan = models.TextField()

    def __str__(self):
        return self.total_pembelian


class Detail_Penjualan(models.Model):
    penjualan_id = models.ForeignKey(Penjualan, on_delete=models.CASCADE)
    barang_id = models.ForeignKey(Barang, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        return self.penjualan_id
