# Create your views here.
from django.shortcuts import render

from .models import DIAS

def votacao(request):
    template_name = 'votacao/home.html'
    return render(request, template_name)
    
def criar_votacao(request):
    queryset = [dict(id=id, nome=nome) for id, nome in DIAS]
    template_name='votacao/criarvotacao.html'
    return render(request, template_name, {'object_list': queryset})
