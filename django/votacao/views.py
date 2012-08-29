# Create your views here.
from django.shortcuts import render

def votacao(request):
    v = 1
    return render(request, 'votacao/home.html', {'v': 'v'})
