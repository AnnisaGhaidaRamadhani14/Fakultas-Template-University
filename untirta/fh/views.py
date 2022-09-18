from django.shortcuts import render

# Create your views here.
def prodi2(request):
    return render(request, 'fh/index.html')

def akreditas2(request):
    return render(request, 'fh/akreditas.html')
