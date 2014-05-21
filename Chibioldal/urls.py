from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'recipe.views.home', name='home'),
    url(r'^(?P<id>\d+)', 'recipe.views.post', name='post'),

    url(r'^admin/', include(admin.site.urls)),
)
