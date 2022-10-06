from django.shortcuts import render
from . models import Dosen, Mahasiswa, TenagaPendidik

# Create your views here.
def prodi5(request):
    dosen = Dosen.objects.all()
    tenagapendidik = TenagaPendidik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'dataDosen': dosen,
        'dataTenagaPendidik': tenagapendidik,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fkip/index.html', konteks)

def akreditas5(request):
    return render(request, 'fkip/akreditas.html')