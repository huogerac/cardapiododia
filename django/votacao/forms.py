#coding=utf-8

from django.forms import ModelForm, ValidationError

from datetime import date, datetime

from .models import Votacao

class VotacaoModelForm(ModelForm):
    nome = "a"
    
    class Meta:
        model = Votacao

    def clean_diaDaSemana(self):
        """ atribui o diaDaSemana
            conforme o dataDoAlmoco especificado
        """
        dado = self.cleaned_data['dataDoAlmoco']
        return dado.strftime('%A')
