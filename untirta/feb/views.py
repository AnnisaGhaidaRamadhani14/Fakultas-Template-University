from django.shortcuts import render

# Create your views here.
def prodi1(request):
    return render(request, 'index.html')

def akreditas1(request):
    return render(request, 'akreditas.html')
