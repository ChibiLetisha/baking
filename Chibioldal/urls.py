from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'recipe.views.home', name='home'),
    url(r'^(?P<id>\d+)', 'recipe.views.post', name='post'),
    url(r'^tip/(?P<id>\d+)', 'recipe.views.tip', name='specifictip'),
    url(r'^tips$', 'recipe.views.tips', name='tips'),
    url(r'^newtips$', 'recipe.views.newtips', name='newtips'),
    url(r'^mytips$', 'recipe.views.mytips', name='mytips'),
    url(r'^admin/', include(admin.site.urls)),
)
