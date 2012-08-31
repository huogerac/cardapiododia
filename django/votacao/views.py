# Create your views here.
from django.shortcuts import render

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import DIAS, Votacao, Cardapio

def votacao(request):
    template_name = 'votacao/home.html'
    return render(request, template_name)
    
class VotacaoForm(forms.ModelForm):
    class Meta:
        model = Votacao
            
def criar_votacao(request):

    if request.POST:
        form = VotacaoForm(request.POST)
        if form.is_valid():
            votacao = form.save()
            return HttpResponseRedirect('/votacao/' + str(votacao.id))
    else:
        form = VotacaoForm()
    
    payload = {'form':form }
    return render(request, 'votacao/criarvotacao.html', payload) 

def opcoes_votacao(request, id_votacao):
    votacao = get_object_or_404(Votacao, pk=id_votacao)
    cardapios = Cardapio.objects.filter(dia=votacao.dia)
    return render(request, 'votacao/opcoesvotacao.html', {'votacao': votacao, 'cardapio_list': cardapios})
    
    
