from email import message
from django.shortcuts import render, redirect
from . models import Dosen, Mahasiswa, TenagaPendidik
from fkip.forms import FormDosen, FormDosen, FormTenagaPendidik, FormMahasiswa
from django.contrib import messages

def hapus_dosen(request, id_dosen):
    dosen = Dosen.objects.filter(id=id_dosen)
    dosen.delete()
    if request.method == "POST":
        dosen.hapus()
    
    messages.success(request, "Data berhasil dihapus!")
    return redirect('fkip')

def hapus_tenagapendidik(request, id_tenagapendidik):
    tenagapendidik = TenagaPendidik.objects.filter(id=id_tenagapendidik)
    tenagapendidik.delete()
    if request.method == "POST":
        tenagapendidik.hapus()
    
    messages.success(request, "Data berhasil dihapus!")
    return redirect('fkip')

def hapus_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.filter(id=id_mahasiswa)
    mahasiswa.delete()
    if request.method == "POST":
        mahasiswa.hapus()
    
    messages.success(request, "Data berhasil dihapus!")
    return redirect('fkip')

def ubah_dosen(request, id_dosen):
    dosen = Dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect('ubah_dosen', id_dosen=id_dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form':form,
            'dosen':dosen,
        }
    return render(request, template, konteks)

def ubah_tenagapendidik(request, id_tenagapendidik):
    tenagapendidik = TenagaPendidik.objects.get(id=id_tenagapendidik)
    template = 'ubah-tenagapendidik.html'
    if request.POST:
        form = FormTenagaPendidik(request.POST, instance=tenagapendidik)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect('ubah_tenagapendidik', id_tenagapendidik=id_tenagapendidik)
    else:
        form = FormTenagaPendidik(instance=tenagapendidik)
        konteks = {
            'form':form,
            'tenagapendidik':tenagapendidik,
        }
    return render(request, template, konteks)

def ubah_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.get(id=id_mahasiswa)
    template = 'ubah-mahasiswa.html'
    if request.POST:
        form = FormMahasiswa(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(ubah_mahasiswa, id_mahasiswa=id_mahasiswa)
    else:
        form = FormMahasiswa(instance=mahasiswa)
        konteks = {
            'form':form,
            'mahasiswa':mahasiswa,
        }
    return render(request, template, konteks)
    
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


def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-dosen.html', konteks)
    else:
        form = FormDosen()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-dosen.html', konteks)


def tambah_tenagapendidik(request):
    if request.POST:
        form = FormTenagaPendidik(request.POST)
        if form.is_valid():
            form.save()
            form = FormTenagaPendidik()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-tenagapendidik.html', konteks)
    else:
        form = FormTenagaPendidik()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-tenagapendidik.html', konteks)



def tambah_mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-mahasiswa.html', konteks)
    else:
        form = FormMahasiswa()

        konteks = {
            'form' : form,
        }

    return render(request, 'tambah-mahasiswa.html', konteks)

