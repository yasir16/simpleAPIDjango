from django.db import models

# Create your models here.


class Barang(models.Model):
    name_barang = models.CharField(max_length=100)
    harga_barang = models.FloatField()
    stock_barang = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name_barang

    