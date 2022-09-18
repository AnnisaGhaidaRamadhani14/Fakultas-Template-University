from django.shortcuts import render

# Create your views here.
def prodi3(request):
    return render(request, 'fisip/index.html')

def akreditas3(request):
    return render(request, 'fisip/akreditas.html')