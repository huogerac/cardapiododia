# Create your views here.
from django.shortcuts import render

from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.widgets import HiddenInput
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import ListView

from datetime import date, datetime, time

from .models import Votacao, Cardapio, Voto, Restaurante
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
    
def novo_voto(request, id_votacao):
    votacao_form = get_object_or_404(Votacao, pk=id_votacao)
    restaurante_id = request.POST.get('id_restaurante', None)
    restaurante_form = get_object_or_404(Restaurante, pk=restaurante_id)
    nome_form = request.POST.get('nome', '')
    
    voto = Voto(nome=nome_form, restaurante=restaurante_form, votacao=votacao_form)
    voto.save()
    return HttpResponseRedirect('/votacao/resumo/' + str(votacao_form.id))
    
class VotoListView(ListView):
    template_name='votacao/resumovotacao.html'
    
    def get_queryset(self):
        self.votacao = get_object_or_404(Votacao, pk=self.args[0])
        return Voto.objects.filter(votacao=self.votacao).order_by('restaurante')
    
