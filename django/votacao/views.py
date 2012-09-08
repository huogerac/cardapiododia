# Create your views here.
from django.shortcuts import render

from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.widgets import HiddenInput
from django.shortcuts import render, render_to_response, get_object_or_404

from datetime import date, datetime, time

from .models import Votacao, Cardapio
from .forms import VotacaoModelForm

def home(request):
	menuId = 0
	template_name = 'votacao/home.html'
	return render(request, template_name, {'menuId':menuId})

def sobre(request):
	return render_to_response("votacao/sobre.html")    
    

            
def criar_votacao(request):
	
	menuId = 1

	if request.POST:
		form = VotacaoModelForm(request.POST)
        
		if form.is_valid():
			votacao = form.save()
			return HttpResponseRedirect('/votacao/' + str(votacao.id))
	else:

		hoje = date.today()
		meiodia = datetime.combine(hoje, time(12, 00)) 
		nova_votacao = Votacao(dataDoAlmoco=meiodia)
		form = VotacaoModelForm(instance=nova_votacao)

	form.fields['encerrada'].widget = HiddenInput()
	form.fields['diaDaSemana'].widget = HiddenInput()
	payload = {'form':form, 'menuId':menuId}
	return render(request, 'votacao/criarvotacao.html', payload) 

def opcoes_votacao(request, id_votacao):
	menuId = 1
	votacao = get_object_or_404(Votacao, pk=id_votacao)
	cardapios = Cardapio.objects.filter(dia=votacao.diaDaSemana)
	return render(request, 'votacao/opcoesvotacao.html', {'votacao': votacao, 'cardapio_list': cardapios, 'menuId':menuId})
    
    
