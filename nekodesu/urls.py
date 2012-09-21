from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'vote.views.summary', name='summary'),
    url(r'^everything/$', 'vote.views.everything', name='everything'),
    url(r'^artist/(?P<artist>.+)/$', 'vote.views.artist', name='artist'),
    url(r'^search/(?P<query>.+)/$', 'vote.views.search', name='search'),
    url(r'^info/$', 'vote.views.info', name='info'),
    url(r'^roulette/$', 'vote.views.roulette', name='roulette'),
    url(r'^played/(?P<track_id>.+)/$', 'vote.views.mark_as_played', name='mark_as_played'),

    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^login/', 'django.contrib.auth.views.login'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
