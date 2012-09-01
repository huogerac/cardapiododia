# coding=utf-8

from django.db import models

DIAS_DA_SEMANA = [
    ('segunda', 'Segunda-Feira'),
    ('terca', 'Terca-Feira'),
    ('quarta', 'Quarta-Feira'),
    ('quinta', 'Quinta-Feira'),
    ('sexta', 'Sexta-Feira'),
]

class Restaurante(models.Model):
    nome = models.CharField(max_length=128, db_index=True)
    logotipo = models.FileField(upload_to='logotipo')
    cardapioGeral = models.FileField(upload_to='cardapio')
    
    def __unicode__(self):
        return self.nome  
        
class Cardapio(models.Model):
    restaurante = models.ForeignKey(Restaurante)
    dia = models.CharField(max_length=32, choices=DIAS_DA_SEMANA)
    cardapioDia = models.FileField(upload_to='cardapio')

    def __unicode__(self):
        return self.dia

class Votacao(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=64)
    dataDoAlmoco = models.DateTimeField(u'Data do almoço')
    diaDaSemana = models.CharField(max_length=32, choices=DIAS_DA_SEMANA)
    encerrada = models.BooleanField(default=False)
	
    def __unicode__(self):
        return self.nome
        
class Voto(models.Model):
    nome = models.CharField(max_length=64)
    restaurante = models.ForeignKey(Restaurante)
    votacao = models.ForeignKey(Votacao)
    
    def __unicode__(self):
        return self.nome
