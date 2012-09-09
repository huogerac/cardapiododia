from django.conf.urls import patterns, url

from .views import home, criar_votacao, opcoes_votacao, novo_voto, sobre, VotoListView

urlpatterns = patterns('votacao.views',

    #votacao    
    url(r'^votacao/nova', criar_votacao, name='url_criar_votacao'),
    
    url(r'^votacao/novo_voto/(\d+)', novo_voto, name='url_novo_voto'),
    
    url(r'^votacao/resumo/(\d+)', VotoListView.as_view(), name='url_votacao_resumo'),
    
    url(r'^votacao/(\d+)', opcoes_votacao, name='url_opcoes_votacao'),
    
    url(r'^votacao/sobre', sobre, name='url_sobre'),

	url(r'^votacao/', home, name='url_home'),
    
)
