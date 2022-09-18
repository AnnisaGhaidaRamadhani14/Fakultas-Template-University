from django.shortcuts import render

# Create your views here.
def prodi4(request):
    return render(request, 'fk/index.html')

def akreditas4(request):
    return render(request, 'fk/akreditas.html')