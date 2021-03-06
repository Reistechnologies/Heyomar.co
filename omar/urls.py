from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#Registro de URLS
 
urlpatterns = patterns('',

    

	url(r'^' , include('apps.inicio.urls')) , #about me 
    url(r'^' , include('apps.skills.urls')) , 

 
    # Examples:
    # url(r'^$', 'tributario.views.home', name='home'),
    # url(r'^tributario/', include('tributario.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)



if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )