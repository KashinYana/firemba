from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import main

import settings

urlpatterns = patterns('',
	url(r'^$', main),
    # Examples:
    # url(r'^$', 'firemba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
                 
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.STATIC_ROOT}),     
)
