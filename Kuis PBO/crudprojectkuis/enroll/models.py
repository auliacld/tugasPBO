from django.db import models

# Create your models here.
class User(models.Model):
    nama_barang = models.CharField(max_length=70)
    jumlah_barang = models.CharField(max_length=70)
    harga_barang = models.CharField(max_length=20)
