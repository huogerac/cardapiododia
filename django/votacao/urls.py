from django.conf.urls import patterns, url

from .views import votacao

urlpatterns = patterns('votacao.views',

       #Project    
    url(r'^votacao/', votacao, name='url_votacao'),
    #url(r'^projects', ProjectsListView.as_view(), name='url_project_list'),
    
)
