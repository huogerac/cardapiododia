# coding: utf-8
        
from django.contrib import admin
from django.db.models import TextField
from django.forms import Textarea

from .models import Restaurante, Cardapio
    
#class RestauranteAdmin(admin.ModelAdmin):
#	model = Restaurante

class CardapioInline(admin.TabularInline):
    model = Cardapio

class RestauranteCardapioAdmin(admin.ModelAdmin):
	inlines = [
		CardapioInline,
	]
admin.site.register(Restaurante, RestauranteCardapioAdmin)
#admin.site.register(Restaurante)

    

    
    

