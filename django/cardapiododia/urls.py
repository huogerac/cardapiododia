from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ondealmocar.views.home', name='home'),
    # url(r'^ondealmocar/', include('ondealmocar.foo.urls')),

    # Django Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    #configuracao para ser possivel acessar os arquivos em /media/
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
		{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),    
    
)

urlpatterns += patterns('',
    url(r'', include('votacao.urls')),
)
