from tkinter import PhotoImage
from django.db import models

# Create your models here.
class Dosen(models.Model):
    NIP = models.IntegerField(null=True)
    Nama = models.CharField(max_length=50)
    Tanggal_Lahir = models.CharField(max_length=40)
    Photo = models.CharField(max_length=50)
    Email = models.CharField(max_length=40)
    Fakultas = models.IntegerField(null=True)
    Prodi = models.IntegerField(null=True)
    Alamat_Rumah = models.IntegerField(null=True)

    def __str__(self):
        return self.Nama
