from django.conf.urls import patterns, url

from .views import votacao, criar_votacao

urlpatterns = patterns('votacao.views',

    #votacao    
    url(r'^votacao/nova', criar_votacao, name='url_criar_votacao'),
    url(r'^votacao/', votacao, name='url_votacao'),
    
)
