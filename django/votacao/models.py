from django.db import models

DIAS = [
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
    dia = models.CharField(max_length=32, choices=DIAS)
    cardapioDia = models.FileField(upload_to='cardapio')

    def __unicode__(self):
        return self.dia

class Votacao(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=64)
    dia = models.CharField(max_length=32, choices=DIAS)
	
    def __unicode__(self):
        return self.nome
        
class Voto(models.Model):
    nome = models.CharField(max_length=64)
    restaurante = models.ForeignKey(Restaurante)
    votacao = models.ForeignKey(Votacao)
    
    def __unicode__(self):
        return self.nome
