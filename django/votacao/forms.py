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
		dado = self.cleaned_data['dataDoAlmoco']
		return dado.strftime('%A')
