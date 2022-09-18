import re
from django.shortcuts import render

# Create your views here.
def prodi5(request):
    return render(request, 'fkip/index.html')

def akreditas5(request):
    return render(request, 'fkip/akreditas.html')