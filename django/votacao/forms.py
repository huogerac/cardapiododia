#coding=utf-8

from django.forms import ModelForm, ValidationError

from datetime import date, datetime

from .models import Votacao

from django import forms


class VotacaoModelForm(ModelForm):
    
	dataDoAlmoco = forms.DateTimeField(widget=forms.TextInput(attrs={'data-datepicker':'datepicker'}))
	
	class Meta:
		model = Votacao
        
	def clean_diaDaSemana(self):
		""" atribui o diaDaSemana
			conforme o dataDoAlmoco especificado
		"""
		
		if 'dataDoAlmoco' not in self.cleaned_data:
			raise forms.ValidationError('É necessario preencher a data')
		
		dado = self.cleaned_data['dataDoAlmoco']
		
		return dado.strftime('%A')
		
	#def clean(self):
	#	dataDoAlmoco = self.cleaned_data.get('dataDoAlmoco')
	#	nome = self.cleaned_data.get('nome')
		
		#print '=============>', dataDoAlmoco
		#if dataDoAlmoco is None:
	#		raise forms.ValidationError('É necessario preencher a data')
			
	#	if nome is not None:
	#		raise forms.ValidationError('É necessario preencher nome')
			
		
			
	#	return self.cleaned_data
			
		
		
