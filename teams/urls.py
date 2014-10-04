from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url('^$', 'teams.views.team'),
    url('^player/$', 'teams.views.player'),
)
