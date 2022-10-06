from statistics import mode
from django.db import models

# Create your models here.
class Dosen(models.Model):
    NIP = models.CharField(max_length=500)
    Nama = models.CharField(max_length=500)
    Tanggal_Lahir = models.CharField(max_length=400)
    Photo = models.CharField(max_length=500, null=True)
    Email = models.CharField(max_length=400)
    Fakultas = models.CharField(max_length=500)
    Prodi = models.CharField(max_length=500)
    Alamat_Rumah = models.CharField(max_length=50, blank=True, null=True)

#    def __str__(self):
#       return "{}".format(self.Nama)

class TenagaPendidik(models.Model):
    NIP = models.CharField(max_length=500)
    Nama = models.CharField(max_length=500)
    Tanggal_Lahir = models.CharField(max_length=400)
    Photo = models.CharField(max_length=500)
    Email = models.CharField(max_length=400)
    Unit = models.CharField(max_length=500)
    Alamat_Rumah = models.CharField(max_length=500, blank=True, null=True)

 #   def __str__(self):
#      return "{}".format(self.Nama)
        

class Mahasiswa(models.Model):
    NIM = models.CharField(max_length=500)
    Nama = models.CharField(max_length=500)
    Tanggal_Lahir = models.CharField(max_length=500)
    Photo = models.CharField(max_length=500, null=True)
    Email = models.CharField(max_length=500)
    Fakultas = models.CharField(max_length=500)
    Prodi = models.CharField(max_length=500, blank=True, null=True)

#  def __str__(self):
#       return "{}".format(self.Nama)

        