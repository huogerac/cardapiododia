from django.conf.urls import patterns, url

from .views import votacao, criar_votacao, opcoes_votacao, sobre

urlpatterns = patterns('votacao.views',

    #votacao    
    url(r'^votacao/nova', criar_votacao, name='url_criar_votacao'),
    
    url(r'^votacao/(\d+)', opcoes_votacao, name='url_opcoes_votacao'),
    
    url(r'^votacao/sobre', sobre, name='url_sobre'),

    url(r'^votacao/', votacao, name='url_votacao'),
    
)
